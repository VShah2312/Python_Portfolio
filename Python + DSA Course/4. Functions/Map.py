"""
Map function: 
"""


def change(x):
    return x + 1


a = [12, 43, 54, 654, 6, 1, 3243, 543]
# Map doesnt return a specific data type, its your choice
b = list(map(change, a))
print(b)


def change(x):
    if x % 2 == 0:
        return x + 1
    return x - 1


a = [12, 43, 54, 654, 6, 1, 3243, 543]
b = set(map(change, a))
print(b)
# This doesnt work for any data type as a, b, c will be string then we convert to int.
# a,b,c= int(input("Enter a number seperated by space").split(" "))
# With map we can do this in one step.

# Take multiple input from user seperated by comma:
a = input("Enter a number seperated by space= ")

# Using map function and unpacking:
x, y, z = list(map(int, a.split(" ")))
print(x, type(x))
print(y, type(y))
print(z, type(z))


a, b, c = list(map(int, input("Enter a number seperated by space= ").split(" ")))
print(a, type(a))
print(b, type(b))
print(c, type(c))


a, b, c = map(int, input("Enter a number seperated by space= ").split(" "))
print(a, type(a))
print(b, type(b))
print(c, type(c))
