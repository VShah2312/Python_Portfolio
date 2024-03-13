"""
Question 2: Make a list of your own. Print all the numbers divisible by 3 and 4 in
that list.
"""

a = [3, 6, 9, 12, 18, 24]

for value in a:
    if value % 3 == 0 and value % 4 == 0:
        print(value, end=" ")
print()
