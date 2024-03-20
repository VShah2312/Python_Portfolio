"""
Strings: Data type

1. Immutable. 
2. Almost same as tuple/ list
3. Iterable
"""

a = "python "
b = "is a good language"

# Properties:

# 1. Data type: str
print(a, type(a))

# 2. Adding strings: Concates the two string together.
print(a + b)

# Arithmetic Operations:
# print(a * b)
# print(a * 3) # Only this works.
# print(a - 3)
# print(a - '3')
print(a * 3)

# 3. Indexing:
print(a[0])
# Space also has an index
print(a[-1])

# 4. Traversing/Iteration:
# a. Traversing by Index:
for index in range(0, len(a)):
    print(a[index])
# b. Traversing by Value:
for char in a:  # Keep in mind char is variable name not a data type
    print(char)

# 5. Slicing:
print(a[:])  # Returns whole string
print(a[::-1])  # Reverse string
print(a[::-3])
