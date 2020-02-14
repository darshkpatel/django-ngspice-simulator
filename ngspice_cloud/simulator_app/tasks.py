from celery import shared_task, current_task
from celery import states
from .helpers import ngspice_helpers, graph_plotter
from celery.exceptions import Ignore
import traceback
from upload_app.models import spiceFile
from celery import group

@shared_task
def process_task(task_id):
    file_list = spiceFile.objects.filter(task_id=task_id)
    tasks = []

    for spicefile in file_list:
        file_path = spicefile.file.path
        file_id = spicefile.file_id
        tasks.append(run_simulation.subtask((file_path), task_id=file_id))
    
    job = group(tasks=tasks)
    result = job.apply_async(task_id=task_id)
    return result



@shared_task
def run_simulation(file_path):
    try:
        current_task.update_state(state=states.PROGRESS,
                meta={'current_process': 'Started Processing File'})
        output = ngspice_helpers.ExecNetlist(file_path)
        current_task.update_state(state=states.PROGRESS,
                meta={'current_process': 'Processed Netlist, Loading Plots'})
        graphs = graph_plotter.LoadPSFolder(file_path)
        current_task.update_state(state=states.PROGRESS,
                meta={'current_process': 'Loaded Plots'})
        return output, graphs
    except Exception as e:
        current_task.update_state(state=states.FAILURE, meta={
            'exc_type': type(e).__name__,
            'exc_message': traceback.format_exc().split('\n')})
        print('Exception Occured: ', e)
        raise Ignore()