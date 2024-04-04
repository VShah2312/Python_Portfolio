# Brute Force:
"""
Time Complexity = O(log10 n) where n is the digit
Space Complexity = O(1)
"""


# Better:
def countdigits(num: int):
    c = 0
    n = num
    while n > 0:
        c += 1
        n = n // 10
    return c


print(countdigits(5344))

# Optimal:
"""
Time Complexity = O(1)
Space Complexity = O(1)
"""

import math


def countDigits(num: int):
    return math.ceil(math.log10(num))


print(countDigits(5344))
