import os, sys

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))



def func2():
    print('func2')
    print(os.environ.get('test'))
    print(os.environ['test'])