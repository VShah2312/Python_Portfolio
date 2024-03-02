"""
Question 1: Make a list of your own. Make two more empty list like odd and even.
Put all the even numbers from original list to even and odd numbers to
odd and print both lists. (Don’t remove anything from original one).
"""

a: list[int] = [34, 2323, 3434, 22]

odd = []
even = []

for value in a:
    if value % 2 == 0:
        even.append(value)
    else:
        odd.append(value)
print(even)
print(odd)
