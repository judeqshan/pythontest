#main.py
# import global_vars
from global_vars import my_string
import do_things_module

#Print the instantiated value of the global string
do_things_module.my_function()

#Change the global variable globally
# global_vars.my_string = "goodbye"

my_string = "goodbye"

#Print the new value of the global string
do_things_module.my_function()