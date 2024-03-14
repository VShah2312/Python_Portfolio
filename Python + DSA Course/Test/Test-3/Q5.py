"""
Question 5: Print the following pattern.
* * * * * * * 
  * * * * * 
    * * * 
      * 
"""

num: int = int(input("Enter a number: "))

for i in range(num, 0, -2):
    for k in range(num, i, -2):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Solution:


def pattern(rows: int) -> None:
    for i in range(rows, -1, -1):
        for k in range(rows - i):
            print(" ", end=" ")
        for j in range(2 * i - 1):
            print("*", end=" ")
        print()


pattern(5)
