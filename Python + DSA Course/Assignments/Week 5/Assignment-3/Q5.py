"""
Question 5:  Create a Python function to sort a dictionary by its values. And return
that new dictionary.
"""

from typing import Dict


def sortbyValue(my_dict: Dict) -> Dict:
    result = dict(sorted(my_dict.items(), key=lambda x: x[1]))
    return result


my_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(sortbyValue(my_dict))
