"""
Question 1: 
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""


def pattern(num: int) -> None:
    for i in range(1, num + 1):
        for j in range(1, 6):
            print(j, end=" ")
        print()


pattern(5)
