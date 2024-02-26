"""
Question 5: Create a function addDigits() that takes an integer as an argument.
Calculate the sum of digits of that number.
Example: addDigits(123) -> 6, addDigits(58714)->  25
"""


# With While Loop:
def addDigits_w(n: int) -> int | str:
    if n < 0:
        return "Enter a valid number."
    num = n
    sum = 0
    while True:
        if num // 10 == 0:
            sum += num
            break
        last_digits = num % 10
        num = num // 10
        sum += last_digits
    return sum


n: int = int(input("Enter a number: "))
print(addDigits_w(n))


# With For Loop:
def addDigits_f(n: int) -> int | str:
    if n < 0:
        return "Enter a valid number."
    num = n
    sum = 0
    for i in range(1, len(str(n)) + 1):
        if num // 10 == 0:
            sum += num
            break
        last_digits = num % 10
        num = num // 10
        sum += last_digits
        i += 1
    return sum


n: int = int(input("Enter a number: "))
print(addDigits_f(n))

# Solution :


def addDigits(num: int) -> int:
    # Dont change the num so storing number in n
    n: int = num
    total = 0
    while n > 0:
        total = total + (n % 10)  # n%10 gives us last digit
        n = n // 10
    return total


print(addDigits(123))
print(addDigits(58714))
