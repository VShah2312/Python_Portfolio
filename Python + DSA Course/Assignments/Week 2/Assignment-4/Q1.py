"""
Question 1: Create a function named divs, which will take two parameters n1 and
n2. Return the count of how many numbers from 1 to n1 are divisible by n2.
"""

# With While Loop:


def divs_w(n1: int, n2: int) -> int:
    count = 0
    i = 1
    while i <= n1:
        if i % n2 == 0:
            count += 1
        i += 1
    return count


n1: int = int(input("Enter n1: "))
n2: int = int(input("Enter n2: "))
print(divs_w(n1, n2))


# With For Loop:
def divs_f(n1: int, n2: int) -> int:
    count = 0
    for i in range(1, n1 + 1):
        if i % n2 == 0:
            count += 1
        i += 1
    return count


n1: int = int(input("Enter n1: "))
n2: int = int(input("Enter n2: "))
print(divs_f(n1, n2))
