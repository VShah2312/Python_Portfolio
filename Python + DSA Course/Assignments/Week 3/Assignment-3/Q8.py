"""
Question 8: Create a function findSmallest that accepts an List of Integers and
returns the smallest number from the list.
"""


def findSmallest(a: list) -> int:
    return min(a)


a = [3, 60, 9, 120, 18, 24, 15, 450, -7]
print(findSmallest(a))


def findSmallest_2(a: list) -> int:
    smallest = a[1]
    for i in a:
        if i <= smallest:
            smallest = i
    return smallest


print(findSmallest(a))
