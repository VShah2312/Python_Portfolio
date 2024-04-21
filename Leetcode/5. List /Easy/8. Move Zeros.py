"""
Question: :https://leetcode.com/problems/move-zeroes/
"""

# Brute Force:
# TC: O(N^2)


def moveZeros(nums: list[int]) -> None:
    for i in range(len(nums)):  # TC: O(N)
        for j in range(i + 1, len(nums)):  # TC: O(N)
            if nums[j] != 0 and nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
    return


nums = [0, 1, 0, 3, 12]
moveZeros(nums)
print(nums)
