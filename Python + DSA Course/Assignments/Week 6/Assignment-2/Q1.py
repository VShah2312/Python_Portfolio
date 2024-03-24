"""
Question 1: Write a Python function that takes two numbers as input and returns
the result of their division. Handle the ZeroDivisionError exception if the
second number is zero. If there is ZeroDivisionError, the function should
return -1.
"""


def function(num1: int, num2: int):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return -1


print(function(2, 0))
print(function(2, 2))
