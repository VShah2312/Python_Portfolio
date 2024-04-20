"""
Bubble sort
Time complexity - O(n^2) (Average and worst)
Time complexity - O(n) (Best case)
Space complexity - O(1)
"""


def bubble_sort(arr: list[int]) -> list[int]:  # inplace sort.
    n = len(arr)
    for i in range(n - 2, -1, -1):
        for j in range(
            0, i + 1
        ):  # after each iteration of i we get sorted value from i:,
            # so we dont want j to go till end, its waste.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubble_sort([4, 1, 9, 3, 2, 6]))

# Bubble Sort Implementation with Optimization using flag

"""
Time complexity - O(n^2) (Average and worst)
In the worst-case scenario, the list is in reverse order, 
causing both outer and inner for loop to be executed at fullest.

Time complexity - O(n) (Best case)
In the best-case scenario, the list is already sorted.
This means that during each pass through the list, there are no elements that need to be swapped
When inner for loop will run for first time, the if conditon (if arr[j] > arr[j + 1]:) will never be true
as the list is already sorted and flag 'swap' will remain False indicating no swaps were done
Hence, the inner for loop will get executed only once till 'n-1' which is nothing but first value of 'i'.
O(n-1) ~ O(n)

Space complexity - O(1)
does not require any extra space
"""


def bubble_sort1(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        swap = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                swap = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swap:
            # exits as there were no swaps meaning list is sorted
            return


arr = [64, 25, 12, 22, 11, 27, 0, -15]
bubble_sort1(arr)
print(arr)
