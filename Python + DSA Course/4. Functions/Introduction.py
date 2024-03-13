# Introduction

# What is a function?
# Any task that you might wanna use in future. We create a functions.
# Helps with readability. Easy to change. Efficient. Methods are related to classes.
"""
def greet(): 
    print("Hello World")

This wont return anything till its called. 
"""


def greet():
    print("Hello World!")


greet()


# if you want to use two word for name of a function loginUser. Use uppercase for Secondword first letter.
# registerUserandLogin
# Same naming restriction as variables.
# also keep in mind call functions after function is define else it will throw error.

# Scoping: Mean till where variable is valid.
# Local Variables means valid in those functions only.
# Mean variable is valid only within a particular functions. Globally it will throw error.


def add():
    # Local Variables.
    num1: int = int(input("Enter num1: "))
    num2: int = int(input("Enter num2: "))
    print(num1 + num2)


# This functions doesnt have return statement thus by default it returns none.

# Global Variables now. Even though name is same, they are not same.
num1 = 100
num2 = 200
add()  # Uses local varables (values entered.)
print(num1)
# This will throw error as num1 is local variable. But will use global variables.


# Make 4 functions add, subtract, multiplication and divide.
def add():
    # Local Variables.
    num1: int = float(input("Enter num1: "))
    num2: int = float(input("Enter num2: "))
    print(num1 + num2)


def subtract():
    # Local Variables.
    num1: int = float(input("Enter num1: "))
    num2: int = float(input("Enter num2: "))
    print(num1 - num2)


def product():
    # Local Variables.
    num1: int = float(input("Enter num1: "))
    num2: int = float(input("Enter num2: "))
    print(num1 * num2)


def division():
    # Local Variables.
    num1: int = float(input("Enter num1: "))
    num2: int = float(input("Enter num2: "))
    print(num1 / num2)


def floorDivision():
    pass


# Pass keyword means move on. So for floorDivision function is definied but is pass, as we cant keep it empty.

add()
subtract()
product()
division()
