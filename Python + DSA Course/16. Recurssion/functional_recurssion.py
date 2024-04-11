# Find Sum of first N natural number:


def func(n):
    if n < 0:
        raise Exception("Invalid Value")
    if n == 1:
        return 1  # Base case
    return n + func(n - 1)  # Flow
