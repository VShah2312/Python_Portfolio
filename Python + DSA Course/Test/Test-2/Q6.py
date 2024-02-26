"""
Question 6: Create a function named sumOfSquares, which takes a single integer
as a parameter named n. Return the sum of squares from 1 to n.
"""


def sumOfSquare(n: int) -> int:
    i: int = 1
    sum: int = 0
    while i <= n:
        sum = sum + (i**2)
        i += 1
    return sum


print(sumOfSquare(5))
