"""
Question 4: Write a Python program to reverse a tuple.
"""


def reverse(my_tuple) -> tuple:
    return my_tuple[::-1]


my_tuple = (56, 2, 0, 56, 34, 76, 34, 45, 1, 2, 3)
print(reverse(my_tuple))


# Solution:
from typing import Tuple


def reverseTuple(tup: Tuple) -> Tuple:
    # MEthod 1
    # lst = list(tup)
    # lst.reverse()
    # new_tup = tuple(lst)
    # return new_tup

    return tuple(reversed(tup))


my_tuple = (1, 2, "Anirudh", False, "OK")

r = reverseTuple(my_tuple)
print(r)
