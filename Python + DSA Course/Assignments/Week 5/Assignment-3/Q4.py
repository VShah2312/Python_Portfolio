"""
Question 4:  Write a Python program to Convert two lists into a dictionary
keys = ["One","Two","Three","Four","Five"]
values = [1, 2, 3, 4, 5]
Convert Two List to Dict = {'One' : 1,'Two' : 2,'Three' : 3,'Four' : 4,'Five' : 5}
"""

from typing import Dict


def convertToDict(list1: list, list2: list) -> Dict:
    result = {}
    if len(list1) == len(list2):
        for i in range(0, len(list1)):
            result[list1[i]] = list2[i]
    return result


keys = ["One", "Two", "Three", "Four", "Five"]
values = [1, 2, 3, 4, 5]
print(convertToDict(keys, values))

# Solution:
from typing import Dict, List


def convertToDictionary(lst1: List, lst2: List) -> Dict:
    dictionary = {}
    for i in range(len(lst1)):
        # dictionary.update({lst1[i]: lst2[i]})
        dictionary[lst1[i]] = lst2[i]
    return dictionary


keys = ["One", "Two", "Three", "Four", "Five"]
values = [1, 2, 3, 4, 5]
my_dict = convertToDictionary(keys, values)
print(my_dict)
