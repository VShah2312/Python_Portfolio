"""
Question 4: 
        1 
      2 2 2 
    3 3 3 3 3 
  4 4 4 4 4 4 4 
5 5 5 5 5 5 5 5 5 
  4 4 4 4 4 4 4 
    3 3 3 3 3 
      2 2 2 
        1
"""

# Top half
for i in range(1, 6):
    for j in range(4, i - 1, -1):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print(i, end=" ")
    print()

# Bottom half
for i in range(4, 0, -1):
    for j in range(4, i - 1, -1):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print(i, end=" ")
    print()
