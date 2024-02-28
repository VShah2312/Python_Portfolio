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
    for i in my_list:
        if checkPrime(i):
            print(i, end=" ")
    print()


a = [3, 6, 9, 4, 17, 5, 7, 11, 59, 91]

calulatePrime(a)
