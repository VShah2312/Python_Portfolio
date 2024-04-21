"""
Question: https://www.naukri.com/code360/problems/left-rotate-an-array-by-one_5026278
"""

# Brute Force:
"""
TC: O(N)
SC: O(1)
"""


def rotateArray(arr: list[int], n: int) -> list:
    x = arr.pop(0)  # -> TC: O(N)
    arr.append(x)  # -> TC: O(1)
    return arr


print(rotateArray([1, 2, 3, 4, 5], 5))


# Brute Force 2:
def rotatArray(arr: list[int], n: int) -> list:
    k = arr[0]
    for i in range(len(arr)):
        arr[i] = arr[i + 1]

    arr[-1] = k
    return arr


print(rotateArray([1, 2, 3, 4, 5], 5))
