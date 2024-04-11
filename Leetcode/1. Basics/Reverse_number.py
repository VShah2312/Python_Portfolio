# Optimal:
"""
Time Complexity = O(log10 n), n is the number
Space Complexity = O(1)
"""


def reverseNumberOptimal(num: int) -> int:
    n = num
    reversed_number = 0
    while n > 0:
        last_digit = n % 10
        reversed_number = (reversed_number * 10) + last_digit
        n = n // 10
    return reversed_number


print(reverseNumberOptimal(1234))


# Solution: Leetcode:
class Solution:
    def reverse(self, x: int) -> int:
        n = x
        negative = False
        if n < 0:
            negative = True
            n = n * -1
        result = 0
        while n > 0:
            last_digit = n % 10
            result = (result * 10) + last_digit
            n = n // 10
        if negative:
            if result * -1 < (-(2**31)):
                return 0
            return result * -1

        if result > (2**31) - 1:
            return 0
        return result
