""" 
Properties of List: 

1. Mutuable (which can be changed)
2. Ordered (maintains way users have entered.)
"""

a: list = [78, 67, 44, -100, 87, 321]
print(a)

# Lists are mutable.
# Here we are updating list's position 0, and -1
# We are updating a: list.
a[0] = 100
a[-1] = 100
print(a)

# Gives IndexError:
# a[20] = 20
# print(a)
