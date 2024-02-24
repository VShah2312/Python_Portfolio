"""
Question 1: Create a function named div_by_3_and_5 which takes 2 integers as a
arguments (n1,n2), and print all the numbers divisible by 3 and 5 between
n1 and n2.
"""


def div_by_3_and_5(n1: int, n2: int) -> None:
    if n1 < n2:  # i is smaller and j is larger number.
        i = n1
        j = n2
    else:
        i = n2
        j = n1

    while i <= j:
        if i % 3 == 0 and i % 5 == 0:
            print(i, end=" ")
        i += 1
    print()


n1: int = int(input("Enter n1: "))
n2: int = int(input("Enter n2: "))

div_by_3_and_5(n1, n2)
# print(div_by_3_and_5(n1, n2)) will return non as we dont have return function.
