# Factorial of N:


# Parametrize (forwardtracking):
def func_p(n, f):
    if n < 0:
        raise Exception("Invalid Value")
    if n == 1 or n == 0:
        print(f)
        return
    func_p(n - 1, f * n)


func_p(5, 1)

# Functional:


def func(n):
    if n < 0:
        raise Exception("Invalid Value")
    if n == 1 or n == 0:
        return 1
    return n * func(n - 1)


print(func(5))
