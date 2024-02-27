"""
Question 6: 

"""

# Top Half
for i in range(1, 6):
    for j in range(5, 5 - i, -1):
        print(j, end=" ")
    print()

# Bottom half
for i in range(4, 0, -1):
    for j in range(5, 5 - i, -1):
        print(j, end=" ")
    print()
