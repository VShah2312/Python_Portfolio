"""
Question 8:  Write a function named pattern which accepts an integer n as an
argument. Then print the following pattern.
Example: pattern(4) -> 1 4 9 16, pattern(10)-> 1 4 9 16 25 36 49 64 81 100
"""


# With While Loop:
def pattern_w(n: int) -> None:
    i = 1
    if n <= 0:
        print("Enter a valid number.")
    while i <= n:
        print(i**2, end=" ")
        i += 1
    print()


n: int = int(input("Ente a number: "))
pattern_w(n)
n: int = int(input("Ente a number: "))
pattern_w(n)


# With For Loop:
def pattern_f(n: int) -> None:
    if n <= 0:
        print("Enter a valid number.")
    for i in range(1, n + 1):
        print(i**2, end=" ")
        i += 1
    print()


n: int = int(input("Ente a number: "))
pattern_f(n)
n: int = int(input("Ente a number: "))
pattern_f(n)
