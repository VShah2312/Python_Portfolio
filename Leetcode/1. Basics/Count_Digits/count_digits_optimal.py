"""
Question: https://www.naukri.com/code360/problems/number-of-digits_9173
"""

# Optimal:
"""
Time Complexity = O(1)
Space Complexity = O(1)
"""

import math


def countDigits(num: int):
    return int(math.log10(num)) + 1


print(countDigits(5344))
