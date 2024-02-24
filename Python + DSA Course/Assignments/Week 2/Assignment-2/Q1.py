"""
Question 1: Create a function that takes three numbers as parameters and returns
the largest among them. Also if no arguments are passed, make sure the
parameters take default value as None and return answer as -1.
"""


def largest(n1: int = None, n2: int = None, n3: int = None) -> int:
    if n1 == n2 == n3 == None:
        return -1
    else:
        largest = n1
        if n2 >= largest:
            largest = n2
        if n3 >= largest:
            largest = n3
        return largest


print(largest(3, 4, 1))  # -> 4
print(largest())  # -> -1
