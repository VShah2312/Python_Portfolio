"""
In read mode file has to exists in read mode. But in write mode if file doesnt exist it will create a file in that name. 
You will have close it and then read it doesnt exist. 
"""

f = open("Vrunda.txt", "w")
# Keep in mind using multiple write doesnt mean it will write in different line.
f.write("Vrunda Shah")

f.write("Hello World")
f.close()

# Also if u open file in write mode and you use f.write removes everything in the file and starts writing.

f = open("Vrunda.txt", "a")
# Keep in mind using multiple write doesnt mean it will write in different line.
f.write("Vrunda Shah")

f.write("Hello World")
f.close()
