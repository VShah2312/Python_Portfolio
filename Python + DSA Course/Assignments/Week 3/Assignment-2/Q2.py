"""
Question 2: 
        5 
      5 4 
    5 4 3 
  5 4 3 2 
5 4 3 2 1 
"""


def pattern(num: int) -> None:

    for i in range(1, num + 1):
        for j in range(num - 1, i - 1, -1):
            print(" ", end=" ")
        for k in range(num, num - i, -1):
            print(k, end=" ")
        print()


pattern(6)


def pattern_soln(n: int) -> None:
    for i in range(n, 0, -1):
        for j in range(i - 1):
            print(" ", end=" ")
        for k in range(n, i - 1, -1):
            print(k, end=" ")
        print()


pattern_soln(9)
