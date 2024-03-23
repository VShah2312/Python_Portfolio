"""
Question 2: Write a Python program to count number of items in a dictionary value
that is a list.
"""

from typing import Dict


def countItemsV(my_dict: Dict) -> str:
    sum = 0
    for v in my_dict.values():
        sum += len(v)
    return f"Number of Items in Dictionary: {sum}"


my_dict = {"M1": [67, 79, 90, 73, 36], "M2": [89, 67, 84], "M3": [82, 57]}
print(countItemsV(my_dict))

# Solution:

from typing import Dict


def countItems(dictionary: Dict) -> int:
    count = 0
    for key, value in dictionary.items():
        count = count + len(value)
    return count


result = countItems({"M1": [67, 79, 90, 73, 36], "M2": [89, 67, 84], "M3": [82, 57]})
print(result)
