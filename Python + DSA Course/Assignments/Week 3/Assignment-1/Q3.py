"""
Question 3: 
5 
4 5 
3 4 5
2 3 4 5
1 2 3 4 5
"""


def pattern(num: int) -> None:
    for i in range(1, num + 1):
        for j in range(num + 1 - i, num + 1):
            print(j, end=" ")
        print()


pattern(7)


def pattern_soln(n: int):
    for i in range(n, 0, -1):
        for j in range(i, n + 1):
            print(j, end=" ")
        print()


pattern_soln(7)
