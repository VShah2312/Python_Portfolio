"""
Question: https://www.naukri.com/code360/problems/number-of-digits_9173
"""

# Brute Force:
"""
Time Complexity = O(n) where n is the digit
Space Complexity = O(1)
"""


def countdigits(num: int):
    return len(str(num))  # str -> int, TC:O(N)


print(countdigits(5344))
