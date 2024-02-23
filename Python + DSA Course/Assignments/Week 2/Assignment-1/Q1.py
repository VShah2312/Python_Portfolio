# Question 1: Write a Python function to find the Maximum and minimum of three numbers. Use 3 parameters. Make 2 different functions named as maxi and mini.
def maxi(num1: int = 0, num2: int = 0, num3: int = 0):
    maximum = num1
    if num2 > maximum:
        maxumum = num2
    if num3 > maximum:
        maximum = num3
    print(f"Maximum = {maximum}")


def mini(num1: int = 0, num2: int = 0, num3: int = 0):
    minimum = num1
    if num2 < minimum:
        minimum = num2
    if num3 < minimum:
        minimum = num3
    print(f"Minimum = {minimum}")


maxi(5, -5, -2)
mini(5, -5, -2)
