from typing import List


def alternateNumbers(arr: List[int]) -> List[int]:
    # Write your code here.
    i = 0
    j = 0

    while i < len(arr):
        if arr[i] < 0:
            j = i
            while arr[j] < 0 and j < len(arr) - 1:
                j += 1
            arr[i], arr[j] = arr[j], arr[i]
        i += 1
    return arr


n = 6
arr = [1, 2, -3, -1, -2, 3]

print(alternateNumbers(arr))
