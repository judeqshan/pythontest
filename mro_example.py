################### mro_example.py ###############################
import inspect
from inspect_example import *
 
 
class C:
    pass
 
 
class C_First(C, B):
    pass
 
if __name__ == '__main__':
    #print(inspect.getmro(C_First))
    ancestors = [item.__name__ for item in inspect.getmro(C_First.__class__)]
    print(ancestors)
 