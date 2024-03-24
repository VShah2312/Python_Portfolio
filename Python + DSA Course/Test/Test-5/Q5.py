"""
Question 5: Write a Python program to map two lists into a dictionary. Everything
in both lists should be unique.
"""

list1 = ["red", "green", "blue"]
list2 = ["#FF0000", "#008000", "#0000FF"]


def function(list1: list, list2: list) -> dict:
    result = {}
    for i in range(len(list1)):
        result[list1[i]] = list2[i]
    return result


print(function(list1, list2))

# Solution:
from typing import List, Dict


# Using ZIP, search for ZIP function
def listsToDictionary(list1: List, list2: List) -> Dict | str:
    if len(list1) != len(list2):
        return "Length of List must be the same"
    return dict(zip(list1, list2))


# Normal way
def listsToDictionary2(list1: List, list2: List) -> Dict | str:
    if len(list1) != len(list2):
        return "Length of List must be the same"

    output_dict = {}
    for i in range(len(list1)):
        output_dict[list1[i]] = list2[i]
    return output_dict


list1 = ["red", "green", "blue"]
list2 = ["#FF0000", "#008000", "#0000FF"]

output_dict = listsToDictionary(list1, list2)
print(output_dict)

output_dict = listsToDictionary2(list1, list2)
print(output_dict)
