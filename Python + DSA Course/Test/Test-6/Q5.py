"""
Question 5: Python program to find second largest number in a list. If 2nd largest
element does not exists. Return -1.
"""


def secondLargest(my_list: list[int]) -> int | float:
    Largest = max(my_list)
    result = [i for i in my_list if i != Largest]
    if result == []:
        return -1
    return max(result)


print(secondLargest([1, 2, 3, 4, 5, 6]))
print(secondLargest([1, 1, 1, 1, 1]))
print(secondLargest([1, 2, 74, 23, 556, 8]))
