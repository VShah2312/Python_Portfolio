"""
Question 6: 
5 4 3 2 1
5 4 3 2 
5 4 3 
5 4 
5
"""


def pattern(num: int) -> None:

    for i in range(1, num + 1):
        for j in range(num, i - 1, -1):
            print(j, end=" ")
        print()


pattern(5)
