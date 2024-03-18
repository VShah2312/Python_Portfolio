"""
Question 3: Write a Python program to generate a list of prime numbers less than
500 using list comprehension.
"""


def factors(num: int) -> int:
    i: int = 1
    count: int = 0
    while i <= num:
        if num % i == 0:
            count += 1
        i += 1
    return count


def primeNumbers(num: int) -> list:
    return [i for i in range(1, num) if factors(i) == 2]


print(primeNumbers(500))
