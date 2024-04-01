"""
Question 2: Write a program to generate a list of even numbers between 1 and 20
using list comprehension.
"""


def listOfEven(start: int = 1, end: int = 1) -> list:
    x = [i for i in range(start, end + 1) if i % 2 == 0]
    return x


print(listOfEven(1, 20))
