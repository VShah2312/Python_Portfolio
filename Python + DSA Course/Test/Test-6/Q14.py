"""
Question 14:  Python Program to merge two files into a third file.
"""

with open("hello.txt", "r") as f1, open("hello1.txt", "r") as f2, open(
    "result.txt", "w"
) as f:
    data1 = f1.read()
    data2 = f2.read()
    f.write(data1)
    f.write("\n")
    f.write(data2)
