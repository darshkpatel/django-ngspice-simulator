import os
import subprocess

class CannotAppendPlot(Exception):
    """Base class for exceptions in this module."""
    pass
class CannotRunSpice(Exception):
    """Base class for exceptions in this module."""
    pass

def SetOutput(filepath):
    if os.path.isfile(filepath):
        proc = subprocess.Popen(['sed', '-i','-e', 's/run/set hcopydevtype=postscript\\nset hcopypscolor=1\\nset color0=white\\nset color1=black\\nset color2=red\\nset color3=blue\\nset color4=violet\\nset color5=rgb:3\/8\/0\\nset color6=rgb:4\/0\/0\\nset hcopywidth=800\\nset hcopyheight=600\\nrun\\nhardcopy v.ps allv\\nhardcopy all.ps all\\nhardcopy i.ps alli/', filepath])
        stdout,stderr = proc.communicate()
        if bool(stderr) or proc.returncode==1:
            raise CannotAppendPlot("Sed command did not run successfully")
        else:
            print('Appended Plot')
    else:
        raise IOError

def ExecNetlist(filepath):
    if os.path.isfile(filepath):
        try:
            SetOutput(filepath)
            print('will run ngSpice command')
            proc = subprocess.Popen(['ngspice','-ab',filepath,'-o','output'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout,stderr = proc.communicate()
            print('Ran ngSpice command')

            if  bool(stderr) or (proc.returncode!=0 and proc.returncode!=1):

                print(stderr)
                print(proc.returncode)
                print(stdout)
                target = os.listdir('.')
                for item in target:
                    if (item.endswith(".ps")):
                        os.remove(os.path.join('.', item))
                raise CannotRunSpice("ngspice exited with error")
            else:
                print('Ran ngSpice')
            
            print("Reading Output")
            with open('output','r+') as f:
                output = f.read()
            return output
        except Exception as e:
            print("Encountered Exception:")
            print(e)
        finally:
            target = os.listdir('.')
            os.remove('output')
            for item in target:
                if (item.endswith(".txt")):
                    os.remove(os.path.join('.', item))
            
    else:
        raise IOError
