"""
Question 10: 
1 2 1 2 1
1 2 1 2
1 2 1
1 2 
1
"""

for i in range(1, 6):
    for j in range(1, 7 - i):
        if j % 2 == 0:
            print(2, end=" ")
        else:
            print(1, end=" ")
    print()
