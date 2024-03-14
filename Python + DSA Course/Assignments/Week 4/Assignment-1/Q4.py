"""
Question 4: Make your own list. Write a Python program that takes an integer as an
input, and make a new list containing the last n elements of the original
list. Using slicing logic.
"""

my_list = [10, -5, 8, 3, -1, -9, 7, 2]


def function(my_list: list[int], n: int) -> list:
    result = my_list[len(my_list) - n : :]
    return result


print(function(my_list, 3))
