"""
Tuple is immutable. We can create exactly like a list just use (), instead of [].
Immutable: Means it can't be edited once created. List is mutable. 
"""

from typing import Tuple

my_tuple: tuple[int] = (32, 45, -100, 67, 77, 43)

# Properties:
print(type(my_tuple))
# 1. Access via index similar to list:
print(my_tuple[0])
print(my_tuple[-1])

# 2. Update Index/Value:
# my_tuple[2] = -1
# print(my_tuple)
# Give TypeError: 'tuple' object does not support item assignment

# 3. Traversing/ Iteration:
# a. Traverse by Index:
for index in range(0, len(my_tuple)):
    print(my_tuple[index], end=" ")
print()

# b. Traverse by Value:
for value in my_tuple:
    print(value, end=" ")
print()

# 4. Methods for tuples:
# Can't append, pop, insert etc. as tuple is immutable.
print(my_tuple.count(100))
print(my_tuple.index(43))
# print(my_tuple.index(100)) -> ValueError

# 5. Membership Operators (in, not in)
print("Vrunda" in my_tuple)  # -> bool

# 6. Slicing (We are not changing the tuple, we are creating a new tuple.)
print(my_tuple[1:4])  # -> tuple
print(my_tuple[::-1])  # Reverse tuple.

# 7. Single element tuple:
# We are creating tuple here as well.
a = 98, 0
print(type(a))

# but for single element it doesnt work. It takes as integer. So we need to just add a comma.
a = (0,)
print(type(a))

# 8. Adding two tuples concates the tuples to each other.
my_tuple_2: tuple = (98, 0)
print(my_tuple + my_tuple_2)

# 9. Converting tuple to a list and viceversa:
my_list = list(my_tuple)
print(my_list)
my_tup_conver = tuple(my_list)
print(my_tup_conver)

# 10. Tuple Comprehension: in list we just use [], he we have to convert it to tuple with tuple keyword
a = tuple(i for i in range(1, 11))
print(a)

# 11. Empty tuple:
a = tuple()
print(a)
