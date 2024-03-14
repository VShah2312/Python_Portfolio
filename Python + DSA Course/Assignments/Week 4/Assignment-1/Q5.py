"""
Question 5:  Make your own list. Write a Python program that takes an integer as an
input, and make a new list containing the last n elements of the original list
but in reverse order. Using slicing logic.
"""

my_list = [10, -5, 8, 3, -1, -9, 7, 2]
n = int(input("Enter a number: "))


def function(my_list: list[int], n: int) -> list:
    result = my_list[len(my_list) - n : :]
    result.reverse()
    return result


print(function(my_list, n))
