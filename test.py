import os
import re

with open('test_suit.py', 'r') as f:
    contents = f.readlines()
    print(contents)
    for line in contents:
        
        # print(line)
        pass

for letter in range(97, 123):
    print(chr(letter))