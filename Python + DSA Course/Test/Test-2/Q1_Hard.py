"""
Question 1: Make a function named reverse which accepts an integer n from the
user. Reverse the number passed as a parameter and return the reverse
number. Do not use STRINGS.
"""


def reverse(n: int) -> int | str:
    if n < 0:
        return "Enter a valid number."
    i: int = 1
    num: int = n
    reverse = 0
    while i <= n:
        last_digit = num % 10
        reverse = reverse * 10 + last_digit
        if num // 10 == 0:
            break
        num = num // 10
        i += 1
    return reverse


# print(reverse(1000))
# print(reverse(123))
# print(reverse(1474))
