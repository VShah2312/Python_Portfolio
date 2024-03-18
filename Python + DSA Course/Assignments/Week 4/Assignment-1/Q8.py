"""
Question 8: Write a Python code to split a list into two halves using list slicing.
(Keep the length of list even).
"""


def split(my_list: list[int]) -> list | str:
    if len(my_list) % 2 == 0:
        n = int(len(my_list) / 2)
        result_1 = my_list[:n]
        result_2 = my_list[n:]
        return result_1, result_2
    return "Enter a list with even length"


my_list = [10, -5, 8, 3, -1, -9, 7, 2]
print(split(my_list))

from typing import List


def splitList(lst: List):
    mid: int = len(lst) // 2
    first_half = lst[:mid]
    second_half = lst[mid:]
    print(first_half)
    print(second_half)


my_list = ["Anirudh", 6, 4, 110.654, True, -54]
splitList(my_list)
