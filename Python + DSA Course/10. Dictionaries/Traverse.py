"""
Traverse:
"""

my_dict = {
    "vrunda": 75,
    "akul": 89,
    "muskan": 52,
}

# Method 1:
for key in my_dict:
    print(key, my_dict[key])  # Give key values

# Method 2:
print(my_dict.keys())  # Gives a list of all keys, its iterables.
for k in my_dict.keys():
    print(k, my_dict[k])

# Method 3:
print(my_dict.values())  # Gives a list of all values, its iterable
for value in my_dict.values():
    print(value)

# Keep in mind:
# We can get values using keys but cant get keys from values as values are not unique.

# Method 4: Items
print(my_dict.items())  # Give list of key-value tuple
for i in my_dict.items():
    print(i)  # Gives key-value tuple

for keys, value in my_dict.items():  # Here are unpacking the tuple.
    print(keys, value)
