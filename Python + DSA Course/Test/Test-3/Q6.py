"""
Question 6: Print the following Pattern
*   *   *   * 
  *   *   * 
    *   * 
      * 
    *   * 
  *   *   * 
*   *   *   *
"""

num: int = int(input("Enter a number: "))

# Top half:
for i in range(num, 0, -2):
    for k in range(num, i, -2):
        print(" ", end=" ")
    for j in range(1, i + 1):
        if j % 2 == 0:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()

# Bottom half:
for i in range(1, num - 1, 2):
    for k in range(num - 2, i + 1, -2):
        print(" ", end=" ")
    for j in range(1, i + 3):
        if j % 2 == 0:
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()


# Solution:
def hourglass_pattern(size):
    # Upper half of the hourglass
    for i in range(size, 0, -1):
        for j in range(size - i):
            print(" ", end=" ")
        for j in range(2 * i - 1):
            print("*", end=" ")
        print()

    # Lower half of the hourglass
    for i in range(2, size + 1):
        for j in range(size - i):
            print(" ", end=" ")
        for j in range(2 * i - 1):
            print("*", end=" ")
        print()


hourglass_pattern(5)
