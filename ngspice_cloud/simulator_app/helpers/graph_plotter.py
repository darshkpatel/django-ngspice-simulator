from PIL import Image
import os
def LoadPSFile(path):
    if os.path.isfile(filepath):
        im = Image.open(path)
        return im
    else:
        raise IOError

def LoadPSFolder(path):
    image_objects = []
    if os.path.isdir(filepath):
        target = os.listdir(path)
        for item in target:
            if (item.endswith(".ps")):
                image_objects.append(Image.open(os.path.join(path, item)))
        return image_objects
    else:
        raise IOError
