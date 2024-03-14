"""
Question 2: Write a function named notPrimeNumbers which accepts 2 integers n1
and n2. Print all the numbers from n1 to n2 which are not prime.
Example
notPrimeNumbers(5,20)
6 8 9 10 12 14 15 16 18 20
"""


def factor(n: int) -> int:
    factor = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factor += 1
    return factor


def notPrimeNumbers(n1: int, n2: int) -> None:
    for i in range(n1, n2 + 1):
        if factor(i) != 2:
            print(i, end=" ")
    print()


notPrimeNumbers(1, 10)
notPrimeNumbers(5, 20)


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def notPrimeNumbers_soln(n1: int, n2: int) -> None:
    for num in range(n1, n2 + 1):
        if not is_prime(num):
            print(num, end=" ")
    print()


notPrimeNumbers_soln(1, 10)
notPrimeNumbers_soln(5, 20)
