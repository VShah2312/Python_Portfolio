"""
@ @ @ @ * 
@ @ @ * * 
@ @ * * * 
@ * * * * 
* * * * * 
"""

for i in range(1, 6):
    for j in range(4, i - 1, -1):
        print("@", end=" ")
    print("* " * i)
print()

# Solution :

for i in range(1, 6):
    for j in range(i, 5):
        print("@", end=" ")
    for k in range(1, i + 1):
        print("*", end=" ")
    print()

"""
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
"""

for i in range(1, 6):
    j = 5 - i
    print("  " * j, end=" ")
    print("* " * i)
print()


for i in range(1, 6):
    for j in range(4, i - 1, -1):
        print(" ", end=" ")
    print("* " * i)
