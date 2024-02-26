"""
Question 2: Write a program to display the n terms of a harmonic series and their sum.
1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n terms
Lets suppose n=5.
1/1 + 1/2 + 1/3 + 1/4 + 1/5 = 2.283334
"""


def harmoicSeries_w(n: int) -> str | float:
    if n <= 0:
        return "Enter a valid number."
    i: int = 1
    sum: int = 0
    string = " "
    while i <= n:
        string = string + ("1/" + str(i) + " + ")
        sum = sum + (1 / i)
        i += 1
    return f"{string[:-2]}= {sum:.6f}"


n: int = int(input("Enter a number: "))
print(harmoicSeries_w(n))

# With For Loop:


def harmoicSeries_f(n: int) -> str | float:
    if n <= 0:
        return "Enter a valid number."
    sum = 0
    string = " "
    for i in range(1, n + 1):
        string = string + ("1/" + str(i) + " + ")
        sum = sum + (1 / i)
        i += 1
    return f"{string[:-2]}= {sum:.6f}"


n: int = int(input("Enter a number: "))
print(harmoicSeries_f(n))
