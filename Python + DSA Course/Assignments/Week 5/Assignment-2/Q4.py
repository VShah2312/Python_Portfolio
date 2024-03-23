"""
Question 4: Write a Python function that takes two dictionaries as input, where the
values are lists. The function should merge the lists corresponding to the
same keys in both dictionaries into a single list and return a new dictionary
with these merged lists.
"""

from typing import Dict


def function(dict_1, dict_2) -> dict:
    result = {}
    for key1, value1 in dict_1.items():
        if key1 in dict_2:
            result[key1] = value1 + dict_2[key1]
        if key1 not in dict_2:
            result[key1] = value1
    for key2, value2 in dict_2.items():
        if key2 not in result:
            result[key2] = value2
    return result


d1 = {"A": [1, 2, 3], "B": [4, 5, 6], "C": [1, 4]}
d2 = {"A": [7, 8], "B": [9, 10], "D": [6, 5]}
print(function(d1, d2))


# Solution:
def mergeDictionary(dictionary1, dictionary2):
    merged_dictionary = {}

    # We do this for dictionary1
    for key in dictionary1:
        if key in dictionary2:
            merged_dictionary[key] = dictionary1[key] + dictionary2[key]
        else:
            merged_dictionary[key] = dictionary1[key]

    # Now we do for keys in dictionary2 not present in dictionary1
    for key in dictionary2:
        if key not in dictionary1:
            merged_dictionary[key] = dictionary2[key]

    return merged_dictionary


dict1 = {"x": [1, 2, 3], "y": [4, 5, 6]}
dict2 = {"x": [7, 8, 9], "y": [10, 11, 12], "z": [99, 100, 111]}
result = mergeDictionary(dict1, dict2)
print(result)
print(function(dict1, dict2))
