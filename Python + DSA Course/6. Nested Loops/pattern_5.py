"""
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


def function(n: int) -> None:
    for i in range(1, (n + 3) // 2):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    for i in range(n // 2, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# n=9 nine lines
function(9)

# n=11 eleven lines
function(11)
