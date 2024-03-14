"""
Question 6:  Write a program to remove the nth index element from a list using a
function.
"""


def removeNth(lst: list[int], index) -> list:
    if index >= 0 and len(lst) - 1 < index:
        return "Index does not exists"
    elif index < 0 and len(lst) < -index:
        return "Index does not exists"
    else:
        lst.pop(index)
        return lst


my_list = [9008, 9102, 4311, 222, 98]
print(removeNth(my_list, 6))
print(my_list)
