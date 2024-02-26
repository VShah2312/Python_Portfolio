"""
Question 2: Make a function named checkPalindrome which accepts an integer n
from the user. Return True or False if the number is palindrome or not.
Palindrome means which is same as forward and backwards. Do not use
STRINGS.
"""

from Q1_Hard import reverse


def checkPalindrome(n: int) -> bool:
    return reverse(n) == n


print(checkPalindrome(91))
print(checkPalindrome(1221))
print(checkPalindrome(9854))
print(checkPalindrome(123454321))
