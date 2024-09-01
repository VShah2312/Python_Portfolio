"""https://www.naukri.com/code360/problems/longest-subarray-with-sum-k_5713505"""
from sys import *
from collections import *
from math import *

def getLongestSubarray(nums: [int], k: int) -> int:
    # Your organization's data cannot be pasted here
    sum_map= {}
    sum=0
    max_length=0
    for i in range(len(nums)):
        sum += nums[i]
        if sum ==k:
            max_length= i+1
        remaining = sum -k
        if remaining in sum_map:
            length= i -sum_map[remaining]
            max_length= max(max_length, length)
        if sum not in sum_map:
            sum_map[sum]=i
    return max_length