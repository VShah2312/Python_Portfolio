"""
Question 8: 
1 2 3 4 5
2 3 4 5
3 4 5
4 5 
5
"""


def pattern(num: int) -> None:

    for i in range(1, num + 1):
        for j in range(i, num + 1):
            print(j, end=" ")
        print()


pattern(5)
