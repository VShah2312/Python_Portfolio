"""https://leetcode.com/problems/single-number/description/"""

# TC: O(N)
# SC: O(1)
def getSingleElement(arr : List[int]) -> int:
    # Write your code here.
    for i in range(len(arr)):
        if len(arr)==1:
            return arr[0]
        elif i==0:
            if arr[i] != arr[i+1]:
                return arr[i]
        elif i==len(arr)-1:
            if arr[i-1] != arr[i]:
                return arr[i]
        else:
            if arr[i-1] != arr[i] and arr[i] != arr[i+1]:
                return arr[i]