"""
Question 8: Take 10 integer inputs from user and store them in a list. Now, copy all
the elements in another list but in reverse order.
"""

from copy import copy

i = 1
result = []
while i <= 10:
    num = int(input("Enter a number: "))
    result.append(num)
    i += 1
print(result)
reverse_list = copy(result)
reverse_list.reverse()
print(reverse_list)
