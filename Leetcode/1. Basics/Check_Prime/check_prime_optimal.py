"""
Question: https://www.codingninjas.com/studio/problems/check-prime_624934
"""

"""
Optimal: 
TC -> O(sqrt(n)) where n is the number
SC -> O(1)
"""

from math import sqrt


def checkPrime(num: int) -> bool:
    if num == 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


print(checkPrime(2))
print(checkPrime(3))
print(checkPrime(10))


# Solution:

from math import *
from collections import *
from sys import *
from os import *


## Read input as specified in the question.
## Print output as specified in the question.
def checkPrime(n):
    result = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            result.append(i)
            if n // i != i:
                result.append(n // i)

    if len(result) == 2:
        return "YES"
    return "NO"


n = int(input())
print(checkPrime(n))
