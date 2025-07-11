"""
Merge Sort
Time Complexity: O(n log n) (Best, Average, Worst)
Space Complexity: O(n)
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    i, j = 0, 0

    # Merge the two halves by comparing elements
    while i < len(left) and j < len(right):  # Till either one is exhausted.
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements from left and right halves
    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print(f"Sorted array = {sorted_arr}")


def mergeSort(arr, l: int, r: int):
    # Write Your Code Here
    if len(arr) == 1:
        return arr

    # Dividing the arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = mergeSort(left, 0, len(left) - 1)
    right = mergeSort(right, 0, len(right) - 1)

    return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged


arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = mergeSort(arr, 0, 7)
print(f"Sorted array = {sorted_arr}")
