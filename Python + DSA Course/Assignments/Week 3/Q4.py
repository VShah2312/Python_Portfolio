"""
Question 4: 
5 
4 5 
3 4 5
2 3 4 5
1 2 3 4 5
"""

for i in range(1, 6):
    for j in range(5, 5 - i, -1):
        print(j, end=" ")
    print()
