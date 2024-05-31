""" Question: https://www.naukri.com/code360/problems/check-armstrong_589"""

"""
TC: O(K) where k in number of digits 
SC: O(1)
"""
import math


def checkArmstrong(num):
    # write your code here !!!!!!!!!
    n = num
    k = int(math.log10(n)) + 1
    sum_of_digits = 0
    while n > 0:
        last_digit = n % 10
        sum_of_digits += last_digit**k
        n = n // 10

    return sum_of_digits == num
