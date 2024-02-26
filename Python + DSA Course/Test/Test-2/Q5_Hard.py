"""
Question 5: Make a function named sumOfFirstAndLastDigit which accepts an
integer n from the user. Calculate the sum of first and last digit of a
number and return it.
"""

from Q1_Hard import reverse


def sumOfFirstAndLastDigit(n: int) -> int | str:
    if n < 0:
        return "Enter a valid number. "
    else:
        num: int = n
        sum: int = 0
        if num // 10 == 0:
            sum = num % 10
        else:
            num: int = n
            last_digit = num % 10
            while num >= 10:
                num //= 10
            first_digit = num
            sum = last_digit + first_digit
        return sum


print(sumOfFirstAndLastDigit(1234))
print(sumOfFirstAndLastDigit(8471))
print(sumOfFirstAndLastDigit(5))
print(sumOfFirstAndLastDigit(99))
