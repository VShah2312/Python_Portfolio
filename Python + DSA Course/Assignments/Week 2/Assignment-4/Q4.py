"""
Question 4: Create a function named pattern which takes an integer as an input
and print the following pattern.
Example: pattern(4) -> 10 20 30 40 and pattern(11)-> 10 20 .... 110
"""

# With While Loop:


def pattern_w(n: int) -> None | str:
    i = 1
    if n <= 0:
        print("Enter a valid number")
    while i <= n:
        print(i * 10, end=" ")
        i += 1


print()

n: int = int(input("Enter a number: "))
pattern_w(n)

# With For Loop:


def pattern_f(n: int) -> None | str:
    i = 1
    if n <= 0:
        print("Enter a valid number")
    while i <= n:
        print(i * 10, end=" ")
        i += 1


print()

n: int = int(input("Enter a number: "))
pattern_f(n)
