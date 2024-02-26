"""
Question 5: Make a function named sumPattern that takes an integer n as an
argument from the user. And then calculate the sum of the following
pattern.
"""

from Q4 import factorial


def sumPattern(n: int) -> float | str:
    if n < 0:
        return "Enter a valid number."
    i: int = 1
    sum: int = 0
    while i <= n:
        sum = sum + (1 / factorial(i))
        i += 1
    return sum


print(sumPattern(5))
