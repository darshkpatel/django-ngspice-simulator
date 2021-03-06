from celery import shared_task, current_task
from celery import states
from .helpers import ngspice_helpers, graph_plotter
from celery.exceptions import Ignore
import traceback
from upload_app.models import spiceFile


@shared_task
def process_task(task_id):
    file_list = spiceFile.objects.filter(task_id=task_id)
    print("Processing ", file_list.count(), " Files")

    for spicefile in file_list:
        file_path = spicefile.file.path
        file_id = spicefile.file_id
        print("Processing ", file_path, file_id)
        run_simulation.apply_async(
            kwargs={'file_path': file_path, 'file_id': file_id},
            task_id=file_id)
    return "Processing Files Asynchronously"


@shared_task
def run_simulation(file_path, file_id):
    try:
        print("Processing File at: ", file_path)
        current_task.update_state(
            state='PROGRESS',
            meta={'current_process': 'Started Processing File'}
        )

        output = ngspice_helpers.ExecNetlist(file_path, file_id)

        current_task.update_state(
            state='PROGRESS',
            meta={'current_process': 'Processed Netlist, Loading Plots'}
        )

        graphs = graph_plotter.LoadPSFolder(file_id)
        current_task.update_state(state='PROGRESS',
                                  meta={'current_process': 'Loaded Plots'})
        return output, graphs
    except Exception as e:
        current_task.update_state(state=states.FAILURE, meta={
            'exc_type': type(e).__name__,
            'exc_message': traceback.format_exc().split('\n')})
        print('Exception Occured: ', type(e).__name__)
        raise Ignore()
