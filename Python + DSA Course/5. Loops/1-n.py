# Example 2: Print 1 to n, get n from user.

n: int = int(input("Enter n: "))
i: int = 1
while i <= n:
    print(i, end=" ")
    i += 1
print()  # To get new line.


# How to write above in a function?
n1: int = int(input("Enter n: "))


def printPattern(n: int) -> None:
    i: int = 1
    while i <= n:
        print(i, end=" ")
        i += 1
    print()


printPattern(n1)
