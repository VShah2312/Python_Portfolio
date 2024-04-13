# Reverse a list using recurssion:

# Brute Force soln:


def func(a: list, i: int = 0) -> list:
    a[i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[i]
    return a


my_list = [1, 2, 3, 4]
print(func(my_list, 0))
# my_list[0], my_list[3] = my_list[3], my_list[0]
# my_list[1], my_list[2] = my_list[2], my_list[1]
# print(my_list)
