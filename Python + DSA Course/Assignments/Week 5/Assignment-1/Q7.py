"""
Question 7: Python program to find the size of a Dictionary. Basically print how
many total key-value pair are there.
"""


def sizeDict(my_dict: dict) -> int:
    return len(my_dict.items())


my_dict = {"vrunda": 75, "akul": 89, "muskan": 52, "akul": 34}

print(sizeDict(my_dict))

# OR

print(len(my_dict))

# Solution:

from typing import Dict


def countKeys(dictionary: Dict) -> int:
    return len(dictionary.keys())


print(countKeys({}))
print(countKeys({"name": "xyz"}))
