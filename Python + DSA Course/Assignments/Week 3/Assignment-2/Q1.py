"""
Question 1: 
         1
       2 1
     3 2 1
   4 3 2 1
 5 4 3 2 1
"""

for i in range(1, 6):
    for j in range(4, i - 1, -1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(k, end=" ")
    print()
