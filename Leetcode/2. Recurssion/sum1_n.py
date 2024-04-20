# Find Sum of first N natural number:

# Method 1: Parametrize


def func(i, sum):
    if i < 1:
        print(sum)
        return
    func(i - 1, sum + i)


func(5, 0)
# Find Sum of first N natural number:


def func_2(n):
    if n < 0:
        raise Exception("Invalid Value")
    if n == 1:
        return 1  # Base case
    return n + func_2(n - 1)  # Flow


print(func_2(5))
