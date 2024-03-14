"""
Method of sets: Union and Intersection
"""

a: set = {34, 45, 67, 34, 11}
b: set = {96, 58, 2, 34, 11}

# Union of a and b:
print(a.union(b))

# Returns common elements between a and b:
print(a.intersection(b))

# Addes element to the set:
a.add(-100)
print(a)

# Remove:
# a.remove(21) # Throws keyError
# Behave more like dict keys

# Iteratable:
print(a)
for val in a:
    print(val)

# Membership Operator:
print(33 in a)
