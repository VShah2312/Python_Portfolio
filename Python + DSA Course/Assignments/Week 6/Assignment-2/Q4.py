"""
Question 4: Write a function that takes a list as input and prints the element at
index 5. Handle the IndexError exception if the list doesn't have enough
elements.
"""


def index5(my_list: list):
    try:
        return my_list[5]
    except IndexError:
        return "list doenst have enough elements."


my_list = [0, 1, 2, 3, 4]
print(index5(my_list))


# Solution:
def printElement(input_list: list):
    try:
        element = input_list[5]
        print(f"Element at index 5 is = {element}")
    except IndexError:
        print("The list doesn't have enough elements.")


# Example usage:
my_list = [0, 1, 2, 3, 4]
printElement(my_list)
