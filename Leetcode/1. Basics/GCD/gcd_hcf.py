""" Question : https://www.naukri.com/code360/problems/hcf-and-lcm_840448"""

"""
TC: o(min(n,m))
SC: O(1)
"""


def calcGCD(n: int, m: int) -> int:
    # Write your code here
    i = 1
    gcd = 0
    while n >= i and m >= i:
        if n % i == 0 and m % i == 0:
            gcd = i
        i += 1
    return gcd


print(calcGCD(7, 5))
