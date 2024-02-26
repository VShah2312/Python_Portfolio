"""
Question 4: Make a function named checkArmstrong which accepts an integer n
from the user. Return True or False if that number is an armstrong number.
"""


def Armstrong(n: int) -> int | str:
    if n < 0:
        return "Enter a valid number."
    sum: int = 0
    num: int = n
    while True:
        if num == 0:
            break
        last_digit = num % 10
        num = num // 10
        sum = sum + (last_digit**3)
    return sum


def checkArmstrong(n: int) -> bool:
    return Armstrong(n) == n


print(checkArmstrong(153))
print(checkArmstrong(407))
print(checkArmstrong(127))
