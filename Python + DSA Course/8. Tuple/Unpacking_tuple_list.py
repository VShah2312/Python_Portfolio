"""
Unpacking a tuple/ list: 
"""

my_tuple: tuple[int] = (32, 45, -100, 67, 77, 43)

a: list[int] = [34, 45, 67]
x, y, z = [34, 45, 67]
print(x, type(x))
print(y, type(y))
print(z, type(z))

# If u have more varible on left or more values on right it will give error.
# Keep in mind x,y and z are integers
a, b, c, d = 56, 67, 678, 23  # This tuple unpacking.
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

a, b, c, *d = 56, 67, 678, 23, 45
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(
    d, type(d)
)  # if use * all the extra elements goes in form of list to that variable.

a, b, *c, d = 56, 67, 678, 23, 45
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(
    d, type(d)
)  # if use * all the extra elements goes in form of list to that variable.
