# Iteration/Iterate

# Traverse by indexes:
# We get indexes as well as values by using a[i].

# 1 2 3 4 5
a = [1, 2, 3, 4, 5]
for i in range(0, len(a)):
    print(a[i], end=" ")

i = 0
while i < len(a):
    print(a[i], end=" ")
    i += 1

# 1 3 5
a = [1, 2, 3, 4, 5]
for i in range(0, len(a), 2):
    print(a[i], end=" ")

# Reverse: 5 4 3 2 1
for i in range(-1, -(len(a) + 1), -1):
    print(a[i], end=" ")

for i in range(len(a) - 1, -1, -1):
    print(a[i], end=" ")

# Traverse by Value:
# We get values but not indexes.
a = [78, 67, 44, -100, 87, 321, 543, 56, 6754, 765, 14165.2522]

for i in a:
    print(i)

print(a.index(78))

# Traversing by index/value

for index, value in enumerate(a):
    print(index, value)
