"""
Selection sort
Time complexity - O(n^2)
Space complexity - O(1)
"""


def selection_sort(arr):
    n = len(arr)
    # Traverse through all elements:
    for i in range(0, n):
        # Find the minimum elements in the remaining unsorted array:
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum elements with i the index
        arr[i], arr[min_index] = arr[min_index], arr[i]


arr = [64, 25, 12, 22, 11, -14]
selection_sort(arr)
print(arr)
