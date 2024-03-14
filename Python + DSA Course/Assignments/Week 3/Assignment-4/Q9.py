"""
Question 9: Make a list. Write a simple program for addition of the 2nd element
from start and 2nd element from the end.
"""


def additionElement(list: list[int]) -> int:
    if len(list) == 1:
        print("Cannot add 2nd and last 2nd element as not enough elements in list")
        return
    print(list[1] + list[-2])


my_list = [43, 11, 92, 22]
additionElement(my_list)
