"""
Question 2: Write a Python program to generate a list of factorials less than 1000
using list comprehension.
"""

from typing import List
from math import sqrt


def factorials(num: int) -> list:
    n = 1
    return [n := n * i for i in range(1, num + 1) if n * i < 1000]


print(factorials(100))


# Solution :
def factorial(n: int) -> int:
    total = 1
    for i in range(1, n + 1):
        total = total * i
    return total


def generateFactorialsList(num: int) -> List[int]:
    return [factorial(i) for i in range(1, int(sqrt(num)) + 1) if factorial(i) < num]


x = generateFactorialsList(500)
print(x)
