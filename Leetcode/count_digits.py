"""
Question: count digits x=533356
    Approach: 1 convert number to str and take len 
        int->str tc:O(N), sc: O(1)
"""

# Brute:
x = 5344
print(len(str(x)))


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
import math


def countDigits(num: int):
    return math.ceil(math.log10(num))


print(countDigits(5344))
