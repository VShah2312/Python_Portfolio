"""
Question 8: Create a function findSmallest that accepts an List of Integers and
returns the smallest number from the list.
"""


def findSmallest(a: list[int]) -> int:
    return min(a)


a = [-31, 60, 9, 120, 18, 24, 15, 450, -7]
print(findSmallest(a))


def findSmallest_2(a: list[int]) -> int:
    smallest = a[0]
    for val in a:
        if val <= smallest:
            smallest = val
    return smallest


print(findSmallest(a))
