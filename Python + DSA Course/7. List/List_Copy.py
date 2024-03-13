# Deep and Shallow copy.
a = [56, 56, 69, 1, 2]

b = a
# both will have same id.
print(a, id(a))
print(b, id(b))

b[-1] = 45
# Change will be on both a and b as there id is same.
# We can think we have copied reference not data.

# So to avoid this we use import copy module

from copy import copy, deepcopy

a = [56, 56, 69, 1, 2]

b = copy(a)  # This will be shallow copy
print(a, id(a))
print(b, id(b))

a = [56, 6, 7, [1, 2, 3], 69, 1, 2]
# List has an id but so does each element.
print(a, id(a))
print(a, id(a[3]))

b = copy(a)  # This will be shallow copy
print(a, id(b))
print(b, id(b[3]))  # But this has same id because its a list.
# Thus change in b[3] will also be on a[3]
b[3][1] = 67
print(a)
print(b)

# So in this case we use deepcopy
a = [56, 6, 7, [1, 2, 3], 69, 1, 2]
c = deepcopy(a)

c[3][1] = 67
print(a)
print(c)
