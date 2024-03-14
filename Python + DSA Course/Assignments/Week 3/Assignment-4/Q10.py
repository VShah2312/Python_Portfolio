"""
Question 10: Ask 10 numbers from the user and put them into the list. Now remove
all the even numbers from that list.
"""

from copy import copy

i = 1
result = []
while i <= 3:
    num = int(input("Enter a number: "))
    result.append(num)
    i += 1
print(result)
result_2 = []
for value in result:
    if value % 2 == 1:
        result_2.append(value)

print(result_2)

# Solution
from typing import List


def removeEven(lst: List[int]) -> None:
    result = []
    for i in lst:
        if i % 2 == 1:
            result.append(i)
    print(result)


my_list = []
for _ in range(10):
    num: int = int(input("Enter a number = "))
    my_list.append(num)

removeEven(my_list)
