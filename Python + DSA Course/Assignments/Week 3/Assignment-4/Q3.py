"""
Question 3: Write a Python function that takes two lists and returns True if they
have at least one common element.
Example: 
"""


def isCommon(lst_1: list[int], lst_2: list[int]) -> bool:
    for val in lst_1:
        if val in lst_2:
            return True
    return False


my_list1 = ["Anirudh", "xyz", 98, 11.908, 93, -100]
my_list2 = [9008, 9102, 4311, 222, -100]

print(isCommon(my_list1, my_list2))
