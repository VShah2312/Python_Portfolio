"""
Question 6: Write a program for Sum of number digits in List.
"""


def sumOfDigits(num: int) -> int:
    last_digit = 0
    sum = 0
    while num != 0:
        last_digit = num % 10
        num = num // 10
        sum += last_digit
    return sum


my_list = [12, 67, 98, 34]
result = [sumOfDigits(i) for i in my_list]
print(result)
