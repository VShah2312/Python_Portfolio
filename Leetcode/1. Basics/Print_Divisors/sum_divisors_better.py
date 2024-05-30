"""Question: https://www.naukri.com/code360/problems/sum-of-all-divisors_8360720"""

"""
TC: O(N* sqrt(n))
SC: 0(sqrt(N))
"""

from typing import List


def printDivisors(n: int) -> List[int]:
    # Write your code here
    result = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.append(i)
            if n // i != i:
                result.append(n // i)
    return result


def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    total_sum = 0
    while n > 1:
        total_sum = total_sum + (sum(printDivisors(n)))
        n = n - 1
    return total_sum + 1


# OR
import math


def sumOfAllDivisors(n: int) -> int:
    Sum = 0
    for i in range(1, n + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                Sum += j
                if i // j != j:
                    Sum += i // j
    return Sum
