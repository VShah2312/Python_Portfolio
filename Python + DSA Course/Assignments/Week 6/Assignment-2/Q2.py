"""
Question 2: Write a Python program that asks the user to input their age. Handle
the ValueError exception if the user enters a non-integer value.
"""


def function():
    try:
        age = int(input("Enter your age ="))
        return age
    except ValueError:
        return "Enter a integer value."


print(function())


# Solution:
def getAge():
    try:
        age = int(input("Enter your age = "))
        return age
    except ValueError:
        print("Invalid input. Please enter a valid integer for age.")


age = getAge()
print(f"Age is {age}")
