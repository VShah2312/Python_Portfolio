"""
Question: https://www.naukri.com/code360/problems/ninja-and-the-sorted-check_6581957
"""


def isSorted(n: int, a: list[int]) -> int:
    for i in range(len(a) - 2):
        if a[i] > a[i + 1]:
            return 0
    return 1


print(isSorted(5, [1, 2, 3, 4, 5]))

# Optimal:
"""
Time complexity = O(N) where N is the number of elements in list
Because we looping through the array only once

Space complexity = O(1)
"""

from typing import List


def isSorted(n: int, a: List[int]) -> int:
    for i in range(0, len(a) - 1):
        if a[i] > a[i + 1]:
            return 0
    return 1
