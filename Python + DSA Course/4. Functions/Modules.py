# Modules

""" 
Questions: What is Modules? 
Area file where we save all functions and we can recall it as per our need. 
We saved all the functions in .py
then we can call it by 
1. importing module 
2. module.function
3. To get details about function we can hover over function name
"""
import Area as A

print(A.square(56))
A.rectangle(10, 54.33)
print(A.cirlce(8))
A.rectangle(l=12, b=18)

# Incase wanna call only one function or two function

from Area import rectangle, cirlce
from Area import *  # To import all functions

# Using about method we can directly call function.
rectangle(10, 12)
print(cirlce(5))
