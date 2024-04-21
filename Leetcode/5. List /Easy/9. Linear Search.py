"""
Question: https://www.naukri.com/code360/problems/linear-search_6922070
"""


# Brute Force:
def linearSearch(n: int, num: int, arr: list[int]) -> int:
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1


arr = [6, 7, 8, 4, 1]
num = 4
print(linearSearch(5, num, arr))
