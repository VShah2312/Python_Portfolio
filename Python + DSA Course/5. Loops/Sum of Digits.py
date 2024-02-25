# Example: 123 -> 6, 135 -> 9


def sumOfDigits(num: int) -> int:
    sum = 0
    while True:
        if (
            num // 10 == 0
        ):  # Keep in mind 8//10=0 and 9//10=0, any single digit //10 is zero.
            sum += num
            break
        sum += num % 10
        num = num // 10
    return sum


print(sumOfDigits(123))
print(sumOfDigits(569))
print(sumOfDigits(135))
print(sumOfDigits(111))
