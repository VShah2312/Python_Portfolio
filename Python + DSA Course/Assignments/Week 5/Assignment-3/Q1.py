"""
Question 1: Write a Python script to sort (ascending and descending) a dictionary
by value.
"""

from typing import Dict


def sortAsc(my_dict: Dict) -> Dict:
    result = dict(sorted(my_dict.items(), key=lambda x: x[1]))
    return result


def sortDesc(my_dict: Dict) -> Dict:
    result = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
    return result


my_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(sortAsc(my_dict))
print(sortDesc(my_dict))

# Solution:

from typing import Dict


def sortDictionary(dictionary: Dict, reverse=False):
    return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=reverse))


my_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(f"Ascending order = {sortDictionary(my_dict)}")
print(f"Descending order = {sortDictionary(my_dict,reverse=True)}")
