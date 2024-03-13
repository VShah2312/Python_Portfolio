"""
Question 4: 
        1 
      2 2 2 
    3 3 3 3 3 
  4 4 4 4 4 4 4 
5 5 5 5 5 5 5 5 5 
  4 4 4 4 4 4 4 
    3 3 3 3 3 
      2 2 2 
        1
"""


def pattern(num: int) -> None:

    # Top half
    for i in range(1, num + 1):
        for j in range(num - 1, i - 1, -1):
            print(" ", end=" ")
        for k in range(1, 2 * i):
            print(i, end=" ")
        print()

    # Bottom half
    for i in range(num - 1, 0, -1):
        for j in range(num - 1, i - 1, -1):
            print(" ", end=" ")
        for k in range(1, 2 * i):
            print(i, end=" ")
        print()


pattern(6)


def pattern_soln(n: int) -> None:
    for i in range(1, n // 2 + 2):
        for j in range(n // 2 - i + 1):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print(i, end=" ")
        print()
    for i in range(n // 2, -1, -1):
        for j in range(n // 2 - i + 1):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print(i, end=" ")
        print()


pattern_soln(13)
