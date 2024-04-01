"""
Question 4:Write a function to find the contiguous subarray with the largest sum
in a given list of integers.
"""


def largestSum(my_list: list) -> int:
    Sum_list: list = []
    for sublist in my_list:
        Sum_list.append(sum(sublist))
    return max(Sum_list)


my_list = [[1, 2, 1, 6, 2], [5, 6, 5], [-1, 1, 1, 1, 1]]
print(largestSum(my_list))
