"""
Question 7: Create a function findLargest that accepts an List of Integers and
returns the largest number from the list.
"""


def findLargest(a: list[int]) -> int:
    return max(a)


a = [563, 60, 9, 120, 18, 24, 15, 450]
print(findLargest(a))


def findLargest_2(a: list[int]) -> int:
    largest = a[0]
    for val in a:
        if largest <= val:
            largest = val
    return largest


print(findLargest_2(a))
