"""
Question: https://www.naukri.com/code360/problems/ninja-and-the-second-order-elements_6581960
"""


# Brute force:
def secondOrderElements(n: int, arr: list[int]):
    largest = float("-inf")
    second_largest = float("-inf")
    smallest = float("inf")
    second_smallest = float("inf")
    for nums in arr:
        if nums > second_largest and nums != largest:
            if nums < largest:
                second_largest = nums
            else:
                second_largest = largest
                largest = nums
        if nums < second_smallest and nums != smallest:
            if nums > smallest:
                second_smallest = nums
            else:
                second_smallest = smallest
                smallest = nums
    return [second_largest, second_smallest]


a = [1, 2, 5, 8, 8, 5, 3, 7]
n = len(a)
print(secondOrderElements(n, a))

# Solution:
# Brute force:
"""
Time complexity = O(N logN) where N is the number of elements in list
Space complexity = O(1)
"""

# This method will work only if there are no duplicates in the array
from typing import List


def getSecondOrderElements(n: int, a: List[int]) -> List[int]:
    # Sort the array
    a.sort()

    # Second minimum will be on 1st index
    # Second largest will be on last second index
    return [a[-2], a[1]]


# Better:
"""
We are using 2 for loops, so it will be O(N) + O(N).
Which will be equal to O(2N)
Which then comes down to O(N)

Time complexity = O(N) where N is the number of elements in list
Space complexity = O(1)
"""

# In the previous solution, we were sorting the array, lets try to solve
# without sorting the array and thus descreasing the time complexity

from typing import List


def getSecondOrderElements(n: int, a: List[int]) -> List[int]:
    small = float("inf")
    second_small = float("inf")
    large = float("-inf")
    second_large = float("-inf")

    # Find the smallest and largest number
    for i in range(0, len(a)):
        small = min(small, a[i])
        large = max(large, a[i])

    # Now find the second smallest and second largest
    for i in range(0, len(a)):
        if a[i] < second_small and a[i] != small:
            second_small = a[i]
        if a[i] > second_large and a[i] != large:
            second_large = a[i]
    return [second_large, second_small]


# Optimal:
"""
We are using 1 loop only, so TC will be O(N).

Time complexity = O(N) where N is the number of elements in list
Space complexity = O(1)
"""

# In previous solution we tried to do by 2 FOR loops.
# Can we solve this using single for loop? (Single pass solution?)

from typing import List


def getSecondOrderElements(n: int, a: List[int]) -> List[int]:
    small = float("inf")
    second_small = float("inf")
    large = float("-inf")
    second_large = float("-inf")

    for i in range(0, len(a)):
        if a[i] < small:
            second_small = small
            small = a[i]
        elif a[i] < second_small and a[i] != small:
            second_small = small
        if a[i] > large:
            second_large = large
            large = a[i]
        elif a[i] > second_large and a[i] != large:
            second_large = a[i]

    return [second_large, second_small]
