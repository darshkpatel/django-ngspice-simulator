import os
import subprocess

class CannotAppendPlot(Exception):
    """Base class for exceptions in this module."""
    pass
class CannotRunSpice(Exception):
    """Base class for exceptions in this module."""
    pass

def SetOutput(filepath, plotType='allv'):
    if os.path.isfile(filepath):
        print(' '.join(['sed', '-i','-e', 's/run/run\\nprint '+plotType+ ' > \/tmp\/' +os.path.basename(filepath)+ '_'+plotType+'.txt/', filepath]))
        proc = subprocess.Popen(['sed', '-i','-e', 's/run/run\\nprint '+plotType+ ' > \/tmp\/' +os.path.basename(filepath)+ '_'+plotType+'.txt/', filepath])
        stdout,stderr = proc.communicate()
        print(stdout)
        if bool(stderr):
            raise CannotAppendPlot
        else:
            print('Appended Plot')
    else:
        raise IOError

def ExecNetlist(filepath, plotType='allv'):
    if os.path.isfile(filepath):
        SetOutput(filepath)
        proc = subprocess.Popen(['ngspice','-ab',filepath,'-o','output'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout,stderr = proc.communicate()
        if bool(stderr):
            raise CannotRunSpice
        else:
            print('Ran ngSpice')
        
        print("Reading Output")
        with open('output','r+') as f:
            output = f.read()
        with open('/tmp/' +os.path.basename(filepath)+ '_'+plotType+'.txt','r+') as f:
            plot = f.read()
        return output,plot
            
    else:
        raise IOError
if __name__ == "__main__":
    print(ExecNetlist("./RLC.cir.out"))