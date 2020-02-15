from PIL import Image
import os


def LoadPSFile(path):
    if os.path.isfile(path):
        im = Image.open(path)
        return im
    else:
        raise IOError


def LoadPSFolder(file_id):
    path = '/tmp/ngspice-cloud-temp/'+file_id
    if os.path.isdir(path):
        print('Loading PS Files from ', path)
        image_objects = []
        target = os.listdir(path)
        for item in target:
            if (item.endswith(".ps")):
                print('Plotting ', item)
                ps_path = os.path.join(path, item)
                im = Image.open(str(ps_path))
                print("Opened Image ", ps_path)
                file_path = os.path.join(path, item+'.png')
                im.save(file_path)
                image_objects.append(file_path)
        return image_objects
    else:
        raise IOError('Path Not Directory')
