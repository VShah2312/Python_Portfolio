"""
Question: Add 1 to even numbers and subtract 1 from Odd numbers in the list: 
if i is odd a[i]+=1 else: a[i]-1
"""

a = [78, 67, 44, -100, 87, 321]

for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i] += 1
    else:
        a[i] -= 1
print(a)

# OR

a = [78, 67, 44, -100, 87, 321]

for index, value in enumerate(a):
    if value % 2 == 0:
        a[index] += 1
    else:
        a[index] -= 1
print(a)

"""
Question: Add 1 to numbers at even index and subtract 1 from numbers at odd index in the list: 
"""

for i in range(len(a)):
    if i % 2 == 0:
        a[i] += 1
    else:
        a[i] -= 1
print(a)
