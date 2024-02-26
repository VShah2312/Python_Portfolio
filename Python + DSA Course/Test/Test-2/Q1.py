"""
Question 1: Create a function named as checkPrime that takes an integer as an
argument. Print YES if the number passed is a prime number else print NO.
"""


def factors(n: int) -> int | str:
    if n <= 0:
        return "Enter a valid number."
    i: int = 1
    count: int = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count


def checkPrime(n: int) -> bool | str:
    if n <= 0:
        return "Enter a valid number."
    return factors(n) == 2


# Q1 Specific
# n: int = int(input("Enter a number: "))
# if checkPrime(n):
#     print("Yes")
# else:
#     print("No")
