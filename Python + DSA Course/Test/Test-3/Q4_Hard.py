"""
Question 4: Write a Python code to check if a list is a palindrome (reads the same
forwards and backwards). Just print “YES” or “NO”
"""

a = [0, 1, 2, 1, 0]


def palindrome(a: list[int]) -> str:
    for i in range(len(a)):
        if a[i] != a[len(a) - 1 - i]:
            return "NO"
        return "YES"


print(palindrome(a))
