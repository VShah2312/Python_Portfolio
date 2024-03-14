"""
Question 4:  Write a Python Program to find sum and average of List in Python.
"""

from typing import List


def sumList(lst: list[int]) -> float | int:
    sum = 0
    for val in lst:
        sum += val
    return sum


def avgList(lst: list[int]) -> float | int:
    sum = sumList(lst)
    avg = sum / len(lst)
    return avg


my_list: List[int | float] = [34, 96, 34, 65.34, 51, 27, 96.12, 96, 11, 34]
print(sumList(my_list))
print(avgList(my_list))
