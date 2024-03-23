"""
Compile time: C++, JAVA, it first check/compile the code and then run it. Error is caught during compiling. 

Runtime: Python. It runs line by line and checks the code during running.  

Exception Handling: Its to avoid program from crashing. 
if error occurs in try block, go to except block.  If no error in try block except block won’t run. 
There is always type/name of Error: error message
"""

try:
    print("Hello World")
    print("Good")

except:
    print("Some unkown error occured.")
