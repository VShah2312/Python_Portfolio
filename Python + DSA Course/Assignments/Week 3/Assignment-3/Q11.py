"""
Question 11:Create a function calculatePrime that accepts an List of Integers and
print all the prime numbers in that list.
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


def calulatePrime(my_list: list) -> None:
    for val in my_list:
        if checkPrime(val):
            print(val, end=" ")
    print()


a = [3, 6, 9, 4, 17, 5, 7, 11, 59, 91]

calulatePrime(a)

# Soln:
"""
METHOD 1 (Nested Loops)
"""
from typing import List


def calculatePrime_soln(lst: List[int]) -> None:
    for i in range(0, len(lst)):
        factors = 0
        num = lst[i]
        for j in range(1, num + 1):
            if num % j == 0:
                factors += 1
        if factors == 2:
            print(num, end=" ")


my_list = [34, 11, 91, 59, 33, 22]
calculatePrime_soln(my_list)
