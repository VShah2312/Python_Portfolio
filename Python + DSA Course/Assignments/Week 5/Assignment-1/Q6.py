"""
Question 6: Write a Python program to check if a dictionary is empty or not.
"""

from typing import Dict


def DictLenCheck(my_dict: Dict) -> str:
    if len(my_dict) == 0:
        return "Empty Dictionary"
    return "Not empty dictionary"


subject_marks: Dict[str, int] = {
    "physics": 67,
    "chemistry": 12,
    "english": 95,
    "computer": 99,
    "hindi": 54,
}

a = {}
print(DictLenCheck(subject_marks))
print(DictLenCheck(a))

# Solution:


def isEmpty(dictionary: Dict) -> bool:
    # Method 1 (Best way)
    """
    if not dictionary:
        return True
    return False
    """

    # Method 2
    """
    if len(dictionary.keys()) == 0:
        return True
    return False
    """

    # Method 3
    count = 0
    for i in dictionary.keys():
        count += 1
    if count == 0:
        return True
    return False


print(isEmpty({}))
print(isEmpty({"name": "xyz"}))
