"""
Question 5: Create a function named printPattern that takes one integer (num) as
an argument. Print from -num to num. Also keep in mind number passed as
an argument can be negative or positiv
"""


def printPattern(num: int) -> None:
    if num > 0:
        i = num * -1
        j = num
    else:
        i = num
        j = num * -1

    while i <= j:
        print(i, end=" ")
        i += 1
    print()


num: int = int(input("Enter a number: "))
printPattern(num)
