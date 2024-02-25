"""
Question 3:  Create a function named factorial which takes a integer as an input and
returns the factorial of that number.
Factorial of 5 means 5 x 4 x 3 x 2 x 1 = 120
"""

# With While Loop:


def factorial_w(n: int) -> int | str:
    i = 1
    factorial = 1
    if n < 0:
        return "Enter a valid number"
    while i <= n:
        factorial = factorial * i
        i += 1
    return factorial


n: int = int(input("Enter a number:"))
print(factorial_w(n))


# With For Loop:


def factorial_f(n: int) -> int | str:
    factorial = 1
    if n < 0:
        return "Enter a valid number"
    for i in range(1, n + 1):
        factorial = factorial * i
        i += 1
    return factorial


n: int = int(input("Enter a number:"))
print(factorial_f(n))
