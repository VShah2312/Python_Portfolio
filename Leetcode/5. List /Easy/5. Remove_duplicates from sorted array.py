"""
Question: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""


# Brute force:
def removeDuplicates(nums: list[int]) -> int:
    answer = []
    for i in range(len(nums)):
        if nums[i] not in answer:
            answer.append(nums[i])
    x = [0] * (len(nums) - len(answer))
    answer_x = answer + x
    return len(answer), answer_x


print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
