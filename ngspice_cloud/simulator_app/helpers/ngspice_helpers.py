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
        # print(' '.join(['sed', '-i','-e', 's/run/run\\nprint '+plotType+ ' > \/tmp\/' +os.path.basename(filepath)+ '_'+plotType+'.txt/', filepath]))
        # proc = subprocess.Popen(['sed', '-i','-e', 's/run/run\\nprint '+plotType+ ' > \/tmp\/' +os.path.basename(filepath)+ '_'+plotType+'.txt/', filepath])
        proc = subprocess.Popen(['sed', '-i','-e', 's/run/set hcopydevtype=postscript\\nset hcopypscolor=1\\nset color0=white\\nset color1=black\\nset color2=red\\nset color3=blue\\nset color4=violet\\nset color5=rgb:3\/8\/0\\nset color6=rgb:4\/0\/0\\nset hcopywidth=800\\nset hcopyheight=600\\nrun\\nhardcopy v.ps allv\\nhardcopy all.ps all\\nhardcopy i.ps alli/', filepath])
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
        with open('v.ps','r+') as f:
            plot = f.read()
        return output,plot
            
    else:
        raise IOError


if __name__ == "__main__":
    print(ExecNetlist("./RLC.cir.out"))