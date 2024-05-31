""" Question: https://www.naukri.com/code360/problems/palindrome-number_624662"""

"""
TC: O(K) where k is length of n
SC: O(1) 
"""
n = input()
# taking n as a input
result = n[::-1]
if n == result:
    print("true")
else:
    print("false")
