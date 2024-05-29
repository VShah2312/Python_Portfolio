"""
Question: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""


# Brute force: Doesnt work as we need to make changes in inplace.
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

# Bruteforce:

from typing import List

"""
Time complexity = O(n) where n is the number of elements in list
We are looping two different times, so it will be O(n) + O(n).
Which equals tos O(n)

Space complexity = O(n), suppose all numbers are unique, it will take same length as list
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_dict = dict()
        for i in nums:
            my_dict[i] = 0

        j = 0
        for n in my_dict:
            nums[j] = n
            j += 1
        return j


# Optimal:

from typing import List

"""
Time complexity = O(n) where n is the number of elements in list
But in this case, we are using only 1 loop instead of 2 FOR loops

Space complexity = O(1), no extra space
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        i = 0
        j = i + 1
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
            j += 1
        return i + 1
