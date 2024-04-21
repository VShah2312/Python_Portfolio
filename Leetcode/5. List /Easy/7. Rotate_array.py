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
