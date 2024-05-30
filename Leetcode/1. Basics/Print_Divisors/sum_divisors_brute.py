"""Question: https://www.naukri.com/code360/problems/sum-of-all-divisors_8360720"""

"""
TC: O(N* sqrt(n))
SC: 0(sqrt(N))
"""


def sumOfAllDivisors(n: int) -> int:
    Sum = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                Sum += j
    return Sum
