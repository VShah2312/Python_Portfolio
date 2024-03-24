"""
Question 5: Write a function divide that takes two numbers as input and returns
their division. Call this function with invalid input arguments (e.g., strings
instead of numbers) and handle any exceptions that may occur.
"""


def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Division by zero is not allowed."
    except TypeError:
        return "Invalid input type. Please provide int or float values."


result1 = divide(10, 0)
print(f"Result 1 = {result1}")

result2 = divide("a", 5)
print(f"Result 2 = {result2}")
