"""
Question 7: 
        1 
      1 2 3 
    1 2 3 4 5 
  1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 9 
  1 2 3 4 5 6 7 
    1 2 3 4 5 
      1 2 3 
        1
"""


def pattern(num: int) -> None:
    # Top Half:
    for i in range(1, num + 1):
        for j in range(num - 1, i - 1, -1):
            print(" ", end=" ")
        for k in range(1, 2 * i):
            print(k, end=" ")
        print()
    # Bottom Half:
    for i in range(num - 1, 0, -1):
        for j in range(num, i, -1):
            print(" ", end=" ")
        for k in range(1, 2 * i):
            print(k, end=" ")
        print()


pattern(5)


def pattern_soln(n: int) -> None:
    for i in range(1, n // 2 + 2):
        for j in range(n // 2 - i + 1):
            print(" ", end=" ")
        for k in range(1, 2 * i):
            print(k, end=" ")
        print()
    for i in range(n // 2, -1, -1):
        for j in range(n // 2 - i + 1):
            print(" ", end=" ")
        for k in range(1, 2 * i):
            print(k, end=" ")
        print()


pattern_soln(6)
