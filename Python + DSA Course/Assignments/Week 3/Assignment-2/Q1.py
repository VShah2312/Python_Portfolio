"""
Question 1: 
         1
       2 1
     3 2 1
   4 3 2 1
 5 4 3 2 1
"""


def pattern(num: int) -> None:

    for i in range(1, num + 1):
        for j in range(num - 1, i - 1, -1):
            print(" ", end=" ")
        for k in range(i, 0, -1):
            print(k, end=" ")
        print()


pattern(6)


def pattern_soln(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end=" ")
        for k in range(i, 0, -1):
            print(k, end=" ")
        print()


pattern_soln(9)
