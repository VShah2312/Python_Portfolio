# Reverse a list using recurssion:

# Brute Force soln:


def func(a: list, i: int) -> list:
    if i == len(a) // 2:
        return a
    a[i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[i]
    return func(a, i + 1)


my_list = [1, 2, 3, 4, 5]
print(func(my_list, 0))


# To reverse anywhere in the list:
def reverse_list(lst, start, end):
    if start > end:
        return
    lst[start], lst[end] = lst[end], lst[start]
    reverse_list(lst, start + 1, end - 1)


my_list = [1, 2, 3, 4, 5]
reverse_list(my_list, 2, 3)
print(my_list)  # -> [1, 2, 4, 3, 5], position 2 and 3 is reversed.
