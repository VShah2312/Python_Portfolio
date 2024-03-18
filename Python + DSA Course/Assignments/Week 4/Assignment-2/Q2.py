"""
Question 2: Write a Python program to generate a list of factorials less than 1000
using list comprehension.
"""


def factorials(num: int) -> list:
    n = 1
    return [n := n * i for i in range(1, num + 1) if n * i < 1000]


print(factorials(100))
