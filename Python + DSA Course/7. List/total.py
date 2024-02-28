"""
Sum
"""

a = [78, 67, 44, -100, 87, 321, 543, 56, 6754, 765, 14165.2522]
sum = 0
for i in range(0, len(a)):
    sum += a[i]
print(sum)

total = 0
for i in a:
    total += i
print(total)

a = [78, 67, 44, -100, 87, 33, 31]
total = 0
for i in a:
    if i % 2 == 0:
        total += i
print(total)


total = 0
a = [78, 67, 44, -100, 87, 33, 31]
for i in range(0, len(a)):
    if i % 2 == 0:
        total = total + a[i]
print(total)

total = 0
a = [78, 67, 44, -100, 87, 33, 31]
for i in range(0, len(a), 2):
    total += a[i]
print(total)


total = 0
a = [78, 67, 44, -100, 87, 33, 31]
for i in range(len(a)):
    if i % 2 == 0:
        total = total + a[i]
print(total)
