"""
Question 3: Ask 3 numbers from user. Make a function which returns the middle of
those 3 numbers. Then make a function to check if that middle number is
divisible by both 3 and 4. Make 2 functions for reusability.
"""


def middle(n1: int = 0, n2: int = 0, n3: int = 0):
    print(n1, n2, type(n3))

    if n1 <= n2 <= n3:
        return n2
    elif n2 <= n1 <= n3:
        return n1
    elif n1 <= n3 <= n2:
        return n3


r = middle(1, 8, 0)
print(r)
