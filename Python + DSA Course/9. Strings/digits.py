"""
Question:
Example 1:
    Enter a= python
    Enter b= good
    output: pythongood

Example 2: 
    Enter a= 50
    Enter b=20
    output: 70

Example 3:
    Enter a= python
    Enter b=20
    output: python20
"""

user_input_1: str = input("Enter first input: ")
user_input_2: str = input("Enter second input: ")


def function(user_input_1: str, user_input_2: str) -> str | int:
    if user_input_1.isdigit() and user_input_2.isdigit():
        return int(user_input_1) + int(user_input_2)
    else:
        return user_input_1 + user_input_2


print(function(user_input_1, user_input_2))
