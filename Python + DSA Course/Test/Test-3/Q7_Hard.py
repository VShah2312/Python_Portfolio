"""
Question 7: Write a Python code to find the second largest element in a list without
sorting.
"""

a = [1, 4, 6, 7, 8, 12, 14, 22, 99, 8, 100]
b = a.copy()
largest = a[0]
for i in range(1, len(a)):
    if a[i] > largest:
        largest = a[i]

b.remove(largest)
print(b)
largest_b = b[0]
for i in range(1, len(b)):
    if b[i] > largest_b:
        largest_b = b[i]

print(f" Second largest element: {largest_b}")


# Solution:
from typing import List


def secondLargest(nums: List[int]):
    if len(nums) < 2:
        return "Not enough elements"

    largest = second_largest = float("-inf")  # -inf means the most negative value
    # Can take as the smallest value

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float("-inf"):
        return "There is no second largest element"
    else:
        return second_largest


nums = [12, 74, -89, 96, -98, -96, 52]
result = secondLargest(nums)
print(f"Second largest element = {result}")
