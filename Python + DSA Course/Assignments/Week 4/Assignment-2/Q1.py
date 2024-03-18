"""
Question 1: Write a Python program to generate a list of powers of 2 less than 100
using list comprehension.
"""

from math import sqrt
from typing import List


def generatePowerList(num: int) -> List[int]:
    # return [2**i for i in range(0, num) if 2**i < num]
    return [2**i for i in range(0, int(sqrt(num)) + 1) if 2**i < num]  # More optimal


print(generatePowerList(125))
