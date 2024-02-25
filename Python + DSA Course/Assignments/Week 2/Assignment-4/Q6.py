"""
Question 6: Don’t create a function, just print the following pattern
1 11 111 1111 11111....n times (Ask n from user)
"""

# With While Loop:
n: int = int(input("Enter a number: "))
i = 1
p = 0
while i <= n:
    p = p * 10 + 1
    print(p, end=" ")
    i += 1
print()

# With For Loop:
n: int = int(input("Enter a number: "))
p = 0
for i in range(1, n + 1):
    p = p * 10 + 1
    print(p, end=" ")
    i += 1
print()
