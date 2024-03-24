"""
Question 1: Write a Python function that takes two numbers as input and returns
the result of their division. Handle the ZeroDivisionError exception if the
second number is zero. If there is ZeroDivisionError, the function should
return -1.
"""


def function(num1: int, num2: int):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Division by zero cannot be done.")
        return -1


print(function(2, 0))
print(function(2, 2))


# Solution:
def divide(num1: float, num2: float) -> float | int:
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        print("Division by zero cannot be done.")
        return -1


num1 = float(input("Enter the first number = "))
num2 = float(input("Enter the second number = "))

result = divide(num1, num2)

if result != -1:
    print(f"Result = {result}")
else:
    print("Cannot carry out the division.")
