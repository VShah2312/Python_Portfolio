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

print(f" Second largest {largest_b}")
