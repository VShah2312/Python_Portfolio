"""
Question 7: Create a Python program to find the difference between two
dictionaries.
"""


def difference(dict_1, dict_2):
    result_1 = [i for i in dict_1.keys() if i not in dict_2]
    result_2 = [i for i in dict_2.keys() if i not in dict_1]
    print(f" Keys present only in the first dictionary: {result_1}")
    print(f" Keys present only in the second dictionary: {result_2}")


dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"b": 2, "c": 4, "d": 5}
difference(dict_1, dict_2)

# Solution:


def findDifference(dictionary1, dictionary2) -> None:
    present_in_dict1 = []
    present_in_both = []
    for k in dictionary1:
        if k not in dictionary2:
            present_in_dict1.append(k)
        else:
            present_in_both.append(k)

    present_in_dict2 = []
    for k in dictionary2:
        if k not in dictionary1:
            present_in_dict2.append(k)

    print(f"Keys present only in the first dictionary: {present_in_dict1}")
    print(f"Keys present only in the second dictionary: {present_in_dict2}")
    print(f"Keys present in both dictionaries: {present_in_both}")


findDifference({"a": 1, "b": 2, "c": 3}, {"b": 2, "c": 4, "d": 5})
