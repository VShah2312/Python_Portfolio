"""
Question 6: Write a Python program to find the maximum and minimum value in a
dictionary.
"""

from typing import Dict


def max(my_dict: Dict) -> Dict:
    result = [
        sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[0],
    ]
    return dict(result)


my_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(max(my_dict))


def min(my_dict: Dict) -> Dict:
    result = [
        sorted(my_dict.items(), key=lambda x: x[1])[0],
    ]
    return dict(result)


my_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(min(my_dict))

# Solution:

from typing import Dict


def maximum(dictionary: Dict) -> int | float:
    max_num = float("-inf")  # Most negative number
    for v in dictionary.values():
        if v > max_num:
            max_num = v
    return max_num


def minimum(dictionary: Dict) -> int | float:
    min_num = float("inf")  # Most positive number
    for v in dictionary.values():
        if v < min_num:
            min_num = v
    return min_num
