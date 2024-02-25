"""
Question 1: 2 22 222 2222 22222 ... upto n. (Ask n from user)
"""

# With While Loop:


def pattern_w(n: int) -> None:
    i = 1
    p = 0
    while i <= n:
        p = p * 10 + 2
        print(p, end=" ")
        i += 1
    print()


n: int = int(input("Enter a number: "))
pattern_w(n)


# With For Loop:
def pattern_f(n: int) -> None:
    p = 0
    for i in range(1, n + 1):
        p = p * 10 + 2
        print(p, end=" ")
        i += 1
    print()


n: int = int(input("Enter a number: "))
pattern_f(n)
