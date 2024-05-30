""" Question: https://www.naukri.com/code360/problems/count-digits_8416387. 
Find the number of digits of n that evenly divide n.
"""

"""
TC: O(log10 n)
SC: 0(1)
"""


def countDigits(num: int) -> int:
    n = num
    count = 0
    while n > 0:
        last_digit = n % 10
        if last_digit != 0:
            if num % last_digit == 0:
                count += 1
        n = n // 10
    return count
