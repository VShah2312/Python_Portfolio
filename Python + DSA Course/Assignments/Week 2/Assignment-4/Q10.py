"""
Question 10: Ask a number from user n1. From 1 to n1, print how many prime
numbers are there.
"""

from Q9 import checkPrime_w, checkPrime_f

n: int = int(input("Enter a number: "))

# With While Loop:
i = 1
count = 0
while i <= n:
    if checkPrime_w(i):
        count += 1
    i += 1
print(count)

# With For Loop:
count = 0
for i in range(1, n + 1):
    if checkPrime_f(i):
        count += 1
    i += 1
print(count)
