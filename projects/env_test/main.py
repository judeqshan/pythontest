import os
import sys
# sys.path.append(os.getcwd() + '\\dir1\\dir1_1')
# sys.path.append(os.getcwd() + '\\dir2\\dir2_1')

from test import func

def set_env():
    pass
    os.environ['test'] = 'test1111111111111111111111111'

    python_path = os.environ.get('PYTHONPATH', '')

    # Add the directory to PYTHONPATH
    directory_to_add = os.getcwd() + '\\dir1\\dir1_1'
    os.environ['PYTHONPATH'] = f"{directory_to_add};{python_path}"

    python_path = os.environ.get('PYTHONPATH', '')

    # Add the directory to PYTHONPATH
    directory_to_add = os.getcwd() + '\\dir2\\dir2_1'
    os.environ['PYTHONPATH'] = f"{directory_to_add};{python_path}"

    # from test import func

    
    

def add_sys_path():
    pass
    print(os.getcwd() + '\\dir1\\dir1_1')
   

def get_env():
    pass
    print(os.environ['test'])


if __name__ == "__main__":
    # add_sys_path()
    set_env()
    func()
