"""https://www.naukri.com/code360/problems/longest-subarray-with-sum-k_6682399"""

def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    n= len(a)
    left= 0
    right=0
    max_length=0
    sum=a[0]
    while right <n: 
        while left<= right and sum>k:
            sum-= a[left]
            left +=1
        if sum==k: 
            max_length= max(max_length, right-left+1)
        right +=1
        if right<n:
            sum += a[right]
    return max_length
