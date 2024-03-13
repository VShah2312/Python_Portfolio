"""
Sum
"""

a = [78, 67, 44, -100, 87, 321, 543, 56, 6754, 765, 14165.2522]
sum = 0
for index in range(0, len(a)):
    sum += a[index]
print(sum)

# Sum using values:
total = 0
for value in a:
    total += value
print(total)

# Total of all even numbers in the list:
a = [78, 67, 44, -100, 87, 33, 31]
total = 0
for value in a:
    if value % 2 == 0:
        total += value
print(total)

# Total of all numbers at even index:
total = 0
a = [78, 67, 44, -100, 87, 33, 31]
for i in range(0, len(a)):
    if i % 2 == 0:
        total = total + a[i]
print(total)

# OR

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
