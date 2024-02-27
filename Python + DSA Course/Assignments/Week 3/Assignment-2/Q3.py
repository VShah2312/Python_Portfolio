"""
Question 3: 
"""

for i in range(1, 6):
    for j in range(4, i - 1, -1):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print(i, end=" ")
    print()
