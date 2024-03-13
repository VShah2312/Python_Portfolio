"""
Question 4: 
5
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1
"""


def pattern(num: int) -> None:
    for i in range(num, 0, -1):
        for j in range(num, i - 1, -1):
            print(j, end=" ")
        print()


pattern(6)
