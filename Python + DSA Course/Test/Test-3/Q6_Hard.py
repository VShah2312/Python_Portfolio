"""
Question 6:  Write a Python code to find the difference between two lists (i.e.,
elements present in the first list but not in the second).
"""

a = [1, 4, 6, 7, 8, 12, 14, 22, 99, 8, 100]
b = [34, 56, 78, 99, 8, 100]
result = []
for i in range(len(a)):
    if a[i] not in b:
        result.append(a[i])

for i in range(len(b)):
    if b[i] not in a:
        result.append(b[i])

print(result)
