"""https://www.naukri.com/code360/problems/maximum-subarray-sum_630526?leftPanelTabValue=PROBLEM"""

#Brute force: 

def maxSubarraySum(arr, n) :
    maxi= float("-inf")
    for i in range(len(arr)):
        sum =0
        for j in range(i ,len(arr)):
            sum += arr[j]
            maxi= max(maxi, sum)
    return max(maxi,0)
# TC: O(N^2)
# SC: O(1)


# Optimal (Kadane's Algorithm):
def maxSubarraySum(arr, n) :
    maxi= float("-inf")
    sum =0
    for i in range(len(arr)):
        sum += arr[i]
        if sum> maxi: 
            maxi =sum
        if sum<0: 
            sum=0
    return max(maxi, 0)