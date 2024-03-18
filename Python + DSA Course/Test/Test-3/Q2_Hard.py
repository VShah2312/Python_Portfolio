"""
Question 2: Given two sorted lists, write a Python code to merge them into a single
sorted list.

Couldnt do it on my own. 

Thought process: 
"""

from typing import List

a = [1, 4, 4, 6, 7, 8, 12, 14, 22]
b = [4, 34, 56, 78, 99, 100]

i = 0
j = 0

result = []

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    elif b[j] < a[i]:
        result.append(b[j])
        j += 1
    else:  # This covers equal case
        result.append(a[i])  # We are appending both equal elements
        result.append(b[j])
        i += 1
        j += 1

while i < len(a):  # If  len(a) is bigger then len(b)
    result.append(a[i])
    i += 1

while j < len(b):  # If len(b) is bigger then len(a)
    result.append(b[j])
    j += 1

print(result)
