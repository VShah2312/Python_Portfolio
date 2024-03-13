"""
Question 10: 
1 2 1 2 1
1 2 1 2
1 2 1
1 2 
1
"""


def pattern(num: int) -> None:

    for i in range(1, num + 1):
        for j in range(1, num + 2 - i):
            if j % 2 == 0:
                print(2, end=" ")
            else:
                print(1, end=" ")
        print()


pattern(5)


def pattern_soln(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            if j % 2 == 0:
                print(2, end=" ")
            else:
                print(1, end=" ")
        print()


pattern_soln(5)
