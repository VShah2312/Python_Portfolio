"""
Question 6: 
5 
4 5 
3 4 5 
2 3 4 5 
1 2 3 4 5 
2 3 4 5 
3 4 5 
4 5 
5 
"""


def pattern(num: int) -> None:
    # Top half
    for i in range(num, 0, -1):
        for j in range(i, num + 1):
            print(j, end=" ")
        print()

    # Bottom Half
    for i in range(2, num + 1):
        for j in range(i, num + 1):
            print(j, end=" ")
        print()


pattern(5)


def pattern_soln(n: int) -> None:
    for i in range(n // 2 + 1, 0, -1):
        for j in range(i, n // 2 + 2):
            print(j, end=" ")
        print()
    for i in range(2, n // 2 + 2):
        for j in range(i, n // 2 + 2):
            print(j, end=" ")
        print()


pattern_soln(13)
