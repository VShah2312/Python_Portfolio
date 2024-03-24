"""
Question 2: Write a Python program that asks the user to input their age. Handle
the ValueError exception if the user enters a non-integer value.
"""


def function(num1) -> int | str:
    try:
        if type(num1).__name__ == int:
            return num1
    except ValueError:
        return "Enter a integer value."


print(function(1))
print(function("abc"))
