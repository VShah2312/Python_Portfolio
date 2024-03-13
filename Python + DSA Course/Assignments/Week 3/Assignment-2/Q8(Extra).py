"""
Question 8 (Extra): 
5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5
"""


def pattern(num: int) -> None:
    # Top Half
    for i in range(1, num + 1):
        for j in range(5, 5 - i, -1):
            print(j, end=" ")
        print()

    # Bottom half
    for i in range(num - 1, 0, -1):
        for j in range(num, num - i, -1):
            print(j, end=" ")
        print()


pattern(5)
