# My Solution:
"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxi = float("-inf")
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                maxi = max(count, maxi)
                count = 0
            maxi = max(count, maxi)
        return maxi

    # Optimal:
    from typing import List


"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(1)
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                maxi = max(maxi, cnt)
                cnt = 0
        return max(maxi, cnt)
