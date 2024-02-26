"""
Question 4: Ask x and n from user and then calculate the following answer.
Example: pattern(6,4)-> 6^1 - 6^3 + 6^5 - 6^7
         pattern(9,11)-> 9^1 - 9^3 + 9^5 - 9^7.....upto n times
"""

# With While Loop:


def pattern_w(x: int, n: int) -> float | str:
    if x < 0 or n <= 0:
        return "Enter a valid numbers."
    i = 1
    sum = 0
    string = " "
    while i <= n:
        if (-1) ** i == -1:
            string = string + (str(x) + "^" + str(2 * i - 1) + " - ")
        else:
            string = string + (str(x) + "^" + str(2 * i - 1) + " + ")
        sum = sum + (x ** (2 * i - 1)) * ((-1) ** (i + 1))
        i += 1
    return f"{string[:-2]}= {sum}"


x: int = int(input("Enter value for the numerator: "))
n: int = int(input("Enter n: "))
print(pattern_w(x, n))


# With for Loop:
def pattern_f(x: int, n: int) -> float | str:
    if x < 0 or n <= 0:
        return "Enter a valid numbers."
    sum = 0
    string = " "
    for i in range(1, n + 1):
        if (-1) ** i == -1:
            string = string + (str(x) + "^" + str(2 * i - 1) + " - ")
        else:
            string = string + (str(x) + "^" + str(2 * i - 1) + " + ")
        sum = sum + (x ** (2 * i - 1)) * ((-1) ** (i + 1))
        i += 1
    return f"{string[:-2]}= {sum}"


x: int = int(input("Enter value for the numerator: "))
n: int = int(input("Enter n: "))
print(pattern_f(x, n))


# Solution :
def patterSum(x: int, n: int) -> float:
    i: int = 1
    total: float = 0
    y: int = 1
    while i <= n:
        if i % 2 != 0:
            total = total + (x**y)
        else:
            total = total - (x**y)
        y += 2
        i += 1
    return total


print(patterSum(6, 4))
print(patterSum(9, 11))
