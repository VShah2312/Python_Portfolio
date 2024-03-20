"""
Question 4: Ask 5 integers from user. Then ask a single character from user. Print
those integers separated by that character entered by user.
"""

i = 1
result = []

while i <= 5:
    i = int(input("Enter a number: "))
    result.append(i)
    i += 1

char = input("Enter a character: ")
result = char.join(str(i) for i in result)
print(result)

# Solution:
from typing import List


def joinNumbers(numbers: List[int], char: str) -> str:
    return char.join(str(i) for i in numbers)


numbers = []
for i in range(1, 6):
    num = int(input(f"Enter number {i} = "))
    numbers.append(num)

c = input("Enter a character = ")

result = joinNumbers(numbers, c)
print(result)
