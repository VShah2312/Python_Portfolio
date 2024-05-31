"""Question: https://leetcode.com/problems/palindrome-number/"""

"""
TC: O(log N)
SC: O(1)
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # taking n as a input
        ## write your code !!
        num = x
        result = 0
        while num > 0:
            last_digits = num % 10
            result = (result * 10) + last_digits
            num = num // 10
        return result == x
