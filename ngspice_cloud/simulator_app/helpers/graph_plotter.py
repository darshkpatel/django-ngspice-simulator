from PIL import Image
import os
def LoadPSFile(path):
    if os.path.isfile(path):
        im = Image.open(path)
        return im
    else:
        raise IOError

def LoadPSFolder(path):
    if os.path.isdir(os.path.dirname(path)):
        path = os.path.dirname(path)
        print('Loading PS Files from ', path)
        image_objects = []
        target = os.listdir(path)
        for item in target:
            if (item.endswith(".ps")):
                image_objects.append(Image.open(os.path.join(path, item)))
        return image_objects
    else:
        raise IOError('Path Not Directory')

