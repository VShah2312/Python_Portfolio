"""
Question 7: Write a python program to interchange first and last elements in a list.
"""

my_list = [10, -5, 8, 3, -1, -9, 7, 2]


def exchange(my_list: list[int]) -> list:
    x = my_list.pop(0)
    y = my_list.pop(-1)
    my_list.insert(0, y)
    my_list.append(x)
    return my_list


print(exchange(my_list))
