"""
len -> length
max -> maximum
min -> minimum
"""

a = [78, 67, 44, -100, 87, 321, 543, 56, 6754, 765, 14165.2522]
print(f"Length = {len(a)}")
# Will throw error if we have any other data type other than int | float
# If all elements are string, maximum is by ASCII
print(f"Maximum = {max(a)}")
print(f"Minimum = {min(a)}")
print(f"Sum = {sum(a)}")
