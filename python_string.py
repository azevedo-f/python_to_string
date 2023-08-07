import inspect
from python_profile import profileit


def _python_to_string():
 print('python to string example')  
 
@profileit
def get_string():
 sts = inspect.getsource(_python_to_string)
 modified=sts.replace('def _python_to_string():','')
 modified=modified.replace('\n ','\n')
 return modified

sts=get_string()