"""
1. Immutable. 
2. Almost same as tuple/ list
"""

a = "python "
b = "is a good language"

# Data type: str
print(a, type(a))

# Adding strings: Concates the two string together.
print(a + b)

# Arithmetic Operations:
# print(a * b)
# print(a * 3) # Only this works.
# print(a - 3)
# print(a - '3')
print(a * 3)

# Indexing:
print(a[0])
# Space also has an index
print(a[-1])

# We can traverse/ iterate using index:
for index in range(0, len(a)):
    print(a[index])

for char in a:  # Keep in mind char is variable name not a data type
    print(char)

print(a[:])  # Returns whole string
print(a[::-1])  # Reverse string
print(a[::-3])
