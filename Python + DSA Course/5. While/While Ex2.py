# Example 2: Print 1 to n, get n from user.

n: int = int(input("Enter n: "))
i: int = 1
while i <= n:
    print(i)
    i += 1


# How to write above in a function?
def printPattern(n: int) -> None:
    i: int = 1
    while i <= n:
        i += 1
    print(i, end="")
