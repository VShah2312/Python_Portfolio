"""
Question 7: Create a function named as printPrimeFactors that takes an integer n
as a argument and print all the prime factors of that number.
Example if number = 20
Then the factors of 20 are 1,2,5,10,20.
So prime factors are 2,5 (this is the output)
"""

from Q1 import checkPrime


def printPrimeFactors(n: int) -> None:
    if n <= 0:
        print("Enter a valid number.")
    i: int = 1
    while i <= n:
        if n % i == 0:
            if checkPrime(i):
                print(i, end=" ")
        i += 1
    print()


printPrimeFactors(20)
printPrimeFactors(7)
printPrimeFactors(72)
