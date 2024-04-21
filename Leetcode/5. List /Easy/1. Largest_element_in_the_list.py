"""
Question: https://www.naukri.com/code360/problems/largest-element-in-the-array-largest-element-in-the-array_5026279
"""

# Bruteforce:


"""
TC: O(N)
SC: O(1)
"""


def largest(arr: list[int]) -> int:
    return max(arr)


arr = [4, 7, 8, 6, 7, 6]
print(largest(arr))

"""
Time complexity = O(N logN) where N is the number of elements in list
Space complexity = O(1)
"""


def largest(arr: list[int]) -> int:
    # sort the elements first
    arr.sort()
    return arr[-1]


arr = [4, 7, 8, 6, 7, 6]
print(largest(arr))


# Optimal:

"""
Time complexity = O(N) where N is the number of elements in list
Space complexity = O(1)
"""


def largest(arr: list[int]) -> int:
    largest = float("-inf")
    for nums in arr:
        # if nums > largest:
        #     largest = nums
        # instead we can use this
        largest = max(nums, largest)
    return largest


arr = [4, 7, 8, 6, 7, 6]
print(largest(arr))

# Solution:
# Brute Force:

"""
Time complexity = O(N logN) where N is the number of elements in list
Space complexity = O(1)
"""

from sys import *
from collections import *
from math import *


def largestElement(arr, n: int) -> int:
    # Sort the elements first
    arr.sort()

    # Return the largest from the end
    return arr[-1]


# Optimal:

"""
Time complexity = O(N) where N is the number of elements in list
Space complexity = O(1)
"""

from sys import *
from collections import *
from math import *


def largestElement(arr, n: int) -> int:
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num
