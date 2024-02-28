"""
If a[i] is even a[i]+1 else: a[i]-1
"""

a = [78, 67, 44, -100, 87, 321]
print(a)

# Lists are mutable.
# Here we are updating list's position 0, and -1
a[0] = 100
a[-1] = 100
print(a)

a = [78, 67, 44, -100, 87, 321]
for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i] += 1
    else:
        a[i] -= 1
print(a)

a = [78, 67, 44, -100, 87, 321]

for index, value in enumerate(a):
    if value % 2 == 0:
        a[index] += 1
    else:
        a[index] -= 1
print(a)
