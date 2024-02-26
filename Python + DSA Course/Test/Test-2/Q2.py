"""
Question 2:  Print all the prime numbers between 1 to 100.
"""

from Q1 import checkPrime

start: int = int(input("Enter a start number: "))
end: int = int(input("Enter a end number: "))
count: int = 0
i = start
while i <= end:
    if checkPrime(i):
        print(i, end=" ")
        count += 1
    i += 1
print(f"total= {count}")
