# Question 1: Write a Python function to find the Maximum and minimum of three numbers. Use 3 parameters. Make 2 different functions named as maxi and mini.
def maxi(num1: int = 0, num2: int = 0, num3: int = 0):
    maximum = num1
    if num2 > maximum:
        maxumum = num2
    if num3 > maximum:
        maximum = num3
    print(f"Maximum = {maximum}")


# Or you can use max built in function.


def mini(num1: int = 0, num2: int = 0, num3: int = 0):
    minimum = num1
    if num2 < minimum:
        minimum = num2
    if num3 < minimum:
        minimum = num3
    print(f"Minimum = {minimum}")


# Or you can use min built in function.

maxi(5, -5, -2)
mini(5, -5, -2)

# Method 2:


def maxi(a: float, b: float, c: float):
    if a >= b and a >= c:
        print(f"{a} is the maximum number")
    elif b >= c:
        print(f"{b} is the maximum number")
    else:
        print(f"{c} is the maximum number")


def mini(a: float, b: float, c: float):
    if a <= b and a <= c:
        print(f"{a} is the minimum number")
    elif b <= c:
        print(f"{b} is the minimum number")
    else:
        print(f"{c} is the minimum number")


num1: float = 10
num2: float = 5
num3: float = 8

maxi(num1, num2, num3)
mini(num1, num2, num3)
