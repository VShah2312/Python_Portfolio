"""
Question 6:  Write a Python code to find the difference between two lists (i.e.,
elements present in the first list but not in the second).
"""

# Prints all elements in a and not in b
a = [1, 4, 6, 7, 8, 12, 14, 22, 99, 8, 56, 100]
b = [34, 56, 78, 99, 8, 100]
result = []
for i in range(len(a)):
    if a[i] not in b:
        result.append(a[i])
print(result)

# Prints all elements in a and b
a = [1, 4, 6, 7, 8, 12, 14, 22, 99, 8, 100]
b = [34, 56, 78, 99, 8, 100]
result = []
for i in range(len(a)):
    if a[i] in b and a[i] not in result:
        result.append(a[i])

print(result)


# Solution:
from typing import List


def difference(lst1: List, lst2: List):
    for i in lst1:
        if i not in lst2:
            print(i)


difference([1, 2, 3, 4], [3, 4, 5, 6])
