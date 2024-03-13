"""
Question 3: Make a list of your own. Count how many numbers are divisible by 5.
"""

a = [3, 60, 9, 120, 18, 24, 15]
count = 0
for value in a:
    if value % 5 == 0:
        count += 1
print(count)
