"""
Question 5: 
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1
"""


def pattern(num: int) -> None:

    # Top Half
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    # Bottom half
    for i in range(num - 1, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


pattern(7)


def pattern_soln(n: int) -> None:
    for i in range(1, n // 2 + 2):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    for k in range(n // 2, -1, -1):
        for l in range(1, k + 1):
            print(l, end=" ")
        print()


pattern_soln(13)
