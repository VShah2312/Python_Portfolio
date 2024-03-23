"""
Question 8: Create a Python function to reverse a dictionary (swap keys and
values). Make sure the values are different.
"""

from typing import Dict


def swap(my_dict: Dict):
    result = {}
    for key, value in my_dict.items():
        result[value] = key
    return result


my_dict = {"a": 1, "b": 2, "c": 3}
print(swap(my_dict))
