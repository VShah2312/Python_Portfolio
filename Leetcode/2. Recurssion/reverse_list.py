# Reverse a list using recurssion:

# Brute Force soln:


def func(a: list, i: int) -> list:
    if i == len(a) // 2:
        return a
    a[i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[i]
    return func(a, i + 1)


my_list = [1, 2, 3, 4, 5]
print(func(my_list, 0))
