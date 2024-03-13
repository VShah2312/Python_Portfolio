"""
Question 3:
        1 
      2 2 2 
    3 3 3 3 3 
  4 4 4 4 4 4 4 
5 5 5 5 5 5 5 5 5 
"""


def pattern(num: int) -> None:

    for i in range(1, num + 1):
        for j in range(num - 1, i - 1, -1):
            print(" ", end=" ")
        for k in range(1, 2 * i):
            print(i, end=" ")
        print()


pattern(6)


def pattern_soln(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print(i, end=" ")
        print()


pattern_soln(9)
