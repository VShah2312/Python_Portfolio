# Brute Force:
from typing import List

"""
Time complexity -> O(n^2)
n is number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums) + 1):  # -> O(N)
            if i not in nums:  # -> O(N)
                return i


# Better:
from typing import List

"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(n)
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        freq = {i: 0 for i in range(0, len(nums) + 1)}
        for i in nums:
            freq[i] += 1
        for k, v in freq.items():
            if v == 0:
                return k


# Optimal:
from typing import List

"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        original_total = (n * (n + 1)) // 2
        return original_total - sum(nums)


# My solution:
"""
Time complexity -> O(N + N log(N))
n is number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()  # -> O(N log(N))
        for i in range(len(nums)):  # -> O(N)
            if i != nums[i]:
                return i
        return len(nums)
