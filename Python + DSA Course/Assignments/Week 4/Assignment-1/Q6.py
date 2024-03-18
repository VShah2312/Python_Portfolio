"""
Question 6: Make your own list. Write a Python program to reverse that list using
slicing.
"""

my_list = [10, -5, 8, 3, -1, -9, 7, 2]
n = int(input("Enter a number: "))


def function(my_list: list[int], n: int) -> list:
    result = my_list[::-1]
    return result


print(function(my_list, n))

from typing import List


def reverseListSlice(lst: List):
    print(lst[::-1])


my_list = [10, -5, 8, 3, -1, -9, 7, 2]
reverseListSlice(my_list)
