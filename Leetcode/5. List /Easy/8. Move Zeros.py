"""
Question: :https://leetcode.com/problems/move-zeroes/
"""

# Brute Force:
# TC: O(N^2)
# Sc: O(1)


def moveZeros(nums: list[int]) -> None:
    for i in range(len(nums)):  # TC: O(N)
        for j in range(i + 1, len(nums)):  # TC: O(N)
            if nums[j] != 0 and nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
    return


nums = [0, 1, 0, 3, 12]
moveZeros(nums)
print(nums)

from typing import List


# Brute Force:
# TC: O(N^2)
# Sc: O(1)


def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)


nums = [0, 0, 1]
moveZeros(nums)
print(nums)

# Bruteforce:
from typing import List

"""
Time Complexity = O(N), N is length of array
Space Complexity: O(N)
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        temp = []

        # Copy non-zero elements from original to temp array
        for i in range(n):
            if nums[i] != 0:
                temp.append(nums[i])

        # Number of non-zero elements
        nz = len(temp)

        # Copy elements from temp to fill first nz fields of original array
        for i in range(nz):
            nums[i] = temp[i]

        # Fill the rest of the cells with 0
        for i in range(nz, n):
            nums[i] = 0


# Optimal:
# TC: O(N)
# SC: O(1)

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                break
            i += 1
        else:
            return
        j = i + 1
        while j < len(nums):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
