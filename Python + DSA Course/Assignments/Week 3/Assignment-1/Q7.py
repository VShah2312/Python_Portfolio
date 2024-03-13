"""
Question 7: 
5 4 3 2 1
4 3 2 1
3 2 1
2 1 
1
"""


def pattern(num: int) -> None:

    for i in range(1, num + 1):
        for j in range(num + 1 - i, 0, -1):
            print(j, end=" ")
        print()


pattern(5)


def pattern_soln(n: int) -> None:
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


pattern_soln(5)
