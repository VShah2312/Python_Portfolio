"""
Question 2: From 1 to 2000, print all the LEAP YEARS, using WHILE loop.
"""

# With While loop:


# To check for one year, you enter same starting and ending year.
def checkLeapYear_w(n1: int, n2: int) -> None:
    i = n1
    while i <= n2:
        if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
            print(i, end=" ")
        i += 1


print()


# def checkLeapYear_w (year:int)-> bool:
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# checkLeapYear_w(1, 2000)
# checkLeapYear_w(1990, 2000)
checkLeapYear_w(2000, 2000)


# With For  loop:
def checkLeapYear_f(n1: int, n2: int) -> None:
    for i in range(n1, n2 + 1):
        if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
            print(i, end=" ")
        i += 1


print()


# checkLeapYear_f(1, 2000)
# checkLeapYear_f(1990, 2000)
checkLeapYear_f(2000, 2000)
