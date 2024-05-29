"""
Question: https://leetcode.com/problems/rotate-array/description/
"""


# Brute Force: We are not changing inplace;
def rotate(nums: list[int], k=int) -> list[int]:
    return nums[len(nums) - k :] + nums[: len(nums) - k]


print(rotate([1, 2, 3, 4, 5, 6, 7], 3))


# Brute Force: Inplace
def rotate_2(nums: list[int], k=int) -> list[int]:
    k = k % len(nums)
    while k > 0:
        x = nums.pop()  # TC: -> O(1)
        nums.insert(0, x)  # TC: -> O(N)
        k -= 1
    return


nums = [1, 2, 3, 4, 5, 6, 7]
rotate_2(nums, 3)
print(nums)

# Bruteforce (class):
from typing import List

"""
Time complexity = O(r*n), where r is number of rotations
and n is number of elements in the array

Space complexity = O(1)
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Becuase if k = 8 and length = 7, means
        # we should only rotate 1 time instead of 8 times
        rotations = k % len(nums)

        for _ in range(rotations):
            last = nums.pop()
            nums.insert(0, last)


# Optimal:

from typing import List

"""
Time Complexity = O(n)
Space Complexity = O(1)
"""


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)
        k %= n  # Handle cases where k > n

        reverse(0, n - 1)  # Reverse the entire array
        reverse(0, k - 1)  # Reverse the first k elements
        reverse(k, n - 1)  # Reverse the remaining elements
