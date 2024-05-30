"""
Question: https://www.naukri.com/code360/problems/number-of-digits_9173
"""

"""
Time Complexity = O(log10(n))
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
