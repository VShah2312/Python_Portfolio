"""
Question 1: Write a Python program to get the 4th element from the last element
of a tuple.
"""

from typing import Tuple


def element4(Tuple) -> int:
    return Tuple[-4]


my_tuple = (56, 76, 34, 45, 1, 2, 3)
print(element4(my_tuple))

# Solution:
from typing import Tuple


def fourthElementFromLast(tup: Tuple) -> None:
    if len(tup) < 4:
        print("Not enough elements")
        return

    print(tup[-4])


fourthElementFromLast((1, 2, 3))
fourthElementFromLast((54, 14, 71, 85, 44))
