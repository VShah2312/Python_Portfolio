"""
Question 7: 
"""

# Top Half
for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Bottom half
for i in range(7, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
