"""
Question 6: Print the following Pattern
* * * * 
 * * * * 
  * * * * 
   * * * * 
    * * * * 
"""

for i in range(1, 6):
    for j in range(1, i):
        print("", end=" ")
    for k in range(1, 5):
        print("*", end=" ")
    print()


def pattern(rows: int) -> None:
    for i in range(1, rows):
        for j in range(1, i):
            print(" ", end="")
        for k in range(4):
            print("*", end=" ")
        print()


pattern(5)
