"""
Question 7: Create a function findLargest that accepts an List of Integers and
returns the largest number from the list.
"""


def findLargest(a: list) -> int:
    return max(a)


a = [3, 60, 9, 120, 18, 24, 15, 450]
print(findLargest(a))


def findLargest_2(a: list) -> int:
    largest = a[1]
    for i in a:
        if largest <= i:
            largest = i
    return largest


print(findLargest_2(a))
