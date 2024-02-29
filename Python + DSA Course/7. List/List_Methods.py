# # List Methods

# # Method and functions are 99% same.
# # Method can be specific to a data type

# a = [56, 56, 69, 1, 2]
# # Append to add element at the end of the list. (Pass by reference.)
# a.append(100)
# print(a)

# a.insert(0, 2)
# print(a)

# # Inserts before the index.
# a.insert(3, 5)
# print(a)

# # It added at the end if index is out of the bound.
# a.insert(66, 1000)
# print(a)

# # It inserts to the left of provided position.
# a.insert(-1, 8)
# print(a)


# # Deep and Shallow copy.

# b = a
# # both will have same id.
# print(a, id(a))
# print(b, id(b))

# b[-1] = 45
# # Change will be on both a and b as there id is same.
# # We can think we have copied reference not data.

# # So to avoid this we use import copy module

# from copy import copy, deepcopy

# a = [56, 56, 69, 1, 2]

# b = copy(a)  # This will be shallow copy
# print(a, id(a))
# print(b, id(b))

# a = [56, 6, 7, [1, 2, 3], 69, 1, 2]
# # List has an id but so does each element.
# print(a, id(a))
# print(a, id(a[3]))

# b = copy(a)  # This will be shallow copy
# print(a, id(b))
# print(b, id(b[3]))  # But this has same id because its a list.
# # Thus change in b[3] will also be on a[3]
# b[3][1] = 67
# print(a)
# print(b)

# # So in this case we use deepcopy
# a = [56, 6, 7, [1, 2, 3], 69, 1, 2]
# c = deepcopy(a)

# c[3][1] = 67
# print(a)
# print(c)


# b = a.copy()  # List Method for shallow copy.

# a.clear  # Clears the whole list

a = [56, 56, 69, 1, 2]  # Default is -1
# x = a.pop()  # Default is -1. Removes by index
# print(a)
# y = a.pop(3)
# print(y)
# # z = a.pop(500) # IndexError: pop index out of range
# z = a.pop(-2)
# print(z)

x = a.remove(56)
# Removes by value, if we have multiple value it removes the first occurence.

# del a  # Deletes a value as well as its id.
# a = [56, 56, 69, 1, 2]  # Default is -1

# del a[0]  # We prefer pop.

# a.append([1, 2])  # Appends the list.
# print(a)
# # a.append(1, 2) This doesnt work. and append wants only one argument.
# a.extend([1, 2])  # This works and addes 1 and 2 as elements.
# # Thus we can add multiple values using extend
# # Can't add it using indexes, thus cant add any element in between
# print(a)


# a = [56, 56, 69, 1, 2, "Vrunda"]
# # print(a.sort)  # to sort need one data type.

a = [56, 56, 69, 1, 2]  # hybrid
a.sort()
print(a)
b = a.copy()
# This sorts descending
b.sort(reverse=True)
print(b)

a = [56, 56, 69, 1, 2]
c = a.copy()
# Prints reverse order of elements.
c.reverse()
print(c)
