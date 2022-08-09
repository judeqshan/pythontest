# Python Program to create
# a data type object
import numpy as np
 
# Integer datatype
# guessed by Numpy
x = np.array([1, 2])  
print("Integer Datatype: ")
print(x.dtype)         
 
# Float datatype
# guessed by Numpy
x = np.array([1.0, 2.0]) 
print("\nFloat Datatype: ")
print(x.dtype)  
 
# Forced Datatype
x = np.array([1.0, 2], dtype = np.int64)   
print("\nForcing a Datatype: ")
print(x.dtype)