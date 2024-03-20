"""
Question 2: Write a Python program to find repeated items in a tuple.
"""


def repeated(my_tuple) -> tuple:
    result_2 = []
    result = tuple(i for i in my_tuple if my_tuple.count(i) > 1)
    for val in result:
        if val not in result_2:
            result_2.append(val)
    return tuple(result_2)


my_tuple = (56, 2, 0, 56, 34, 76, 34, 45, 1, 2, 3)
print(repeated(my_tuple))

# Solution:
from typing import Tuple


def findRepeatedElements(t: Tuple):
    repeated_elements = []
    for i in range(len(t)):
        if t[i] in t[i + 1 :] and t[i] not in repeated_elements:
            repeated_elements.append(t[i])
    return repeated_elements


my_tuple = (1, 2, 3, 2, 4, 3, 5, 6, 4)
repeated = findRepeatedElements(my_tuple)
if len(repeated) > 0:
    print(f"Repeated items = {repeated}")
else:
    print("No repeated elements found.")
