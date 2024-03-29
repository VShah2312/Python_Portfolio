"""
Question 1: Write a Python code to check if a given list is sorted in ascending order.

Thought process if element i is bigger then i+1 then its not sorted. 
"""


def function(a: list[int]) -> str:
    num = a[0]
    for i in range(1, len(a)):
        if num > a[i]:
            num = a[i]
            return "NO"
    return "YES"


print(function([1, 3, 4, 5, 6, 12, 19]))
print(function([22, 3, 4, 5, 6, 12, 19]))

from typing import List


def isSorted(lst: List[int]) -> bool:
    for i in range(0, len(lst) - 1):
        if (
            lst[i] > lst[i + 1]
        ):  # Her we dont want to use >= as we want to consider the case where it wont be sorted.
            return False
    return True


print(isSorted([1, 3, 4, 4, 5, 6, 12, 19]))
print(isSorted([22, 3, 4, 5, 6, 12, 19]))
print(sorted([1, 1, 2, 5, 4, 27, 2]))
