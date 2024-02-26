"""
Question 4:  Make a function named factorial(), which takes an integer n. Return the
factorial of that number.
"""


def factorial(n: int) -> int | str:
    if n < 0:
        return "Enter a valid number."
    i: int = 1
    factorial: int = 1
    while i <= n:
        factorial = factorial * i
        i += 1
    return factorial


print(factorial(5))
print(factorial(3))
