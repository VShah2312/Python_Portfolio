"""https://www.naukri.com/code360/problems/reading_6845742"""
# Brute Force

def read(n: int, book: list[int], target: int) -> str:
    # Write your code here.
    for i in range(len(book)):
        for j in range(i+1, len(book)):
            if book[i]+book[j]== target:
                return "YES"
    return "NO"

# TC O(N^2)
# SC: O(1)


# Optimal: 

def read(n: int, arr: list[int], target: int) -> list[int]:
    hash_map={}
    for i in range(len(arr)):
        remaining = target-arr[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        hash_map[arr[i]]= i