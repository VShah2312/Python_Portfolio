"""
Question 5:  Create a function named pattern which takes an integer as an input
and print the following pattern.
Example: pattern(4)-> 1 2 4 8, pattern(7)-> 1 2 4 8 16 32 64
"""

# With While Loop:


def pattern_w(n: int) -> None:
    if n < 0:
        print("Enter a valid number")
    i = 0
    while i < n:
        print(2**i, end=" ")
        i += 1
    print()


n: int = int(input("Enter a number: "))
pattern_w(n)

# With For Loop:


def pattern_f(n: int) -> None:
    if n < 0:
        print("Enter a valid number")
    for i in range(0, n):
        print(2**i, end=" ")
        i += 1
    print()


n: int = int(input("Enter a number: "))
pattern_f(n)
