"""
Question 3:  Make a function named printWords which accepts an integer n from
the user. Print the number as words.
"""

from Q1_Hard import reverse


def numberWords(n: int) -> str:
    if n == 1:
        return "One"
    if n == 2:
        return "Two"
    if n == 3:
        return "Three"
    if n == 4:
        return "Four"
    if n == 5:
        return "Five"
    if n == 6:
        return "Six"
    if n == 7:
        return "Seven"
    if n == 8:
        return "Eight"
    if n == 9:
        return "Nine"
    if n == 0:
        return "Zero"


def printWords(n: int) -> None:
    if n < 0:
        print("Enter a valid number")
    i: int = 1
    num = reverse(n)
    while i <= len(str(n)):
        last_digits = num % 10
        num = num // 10
        print(numberWords(last_digits), end=" ")
        i += 1
    print()


printWords(91)
printWords(1221)
printWords(9854)
printWords(1001)
