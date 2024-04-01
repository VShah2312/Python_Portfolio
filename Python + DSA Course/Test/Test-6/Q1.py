"""
Question 1: Write a function to check if a given string is a palindrome. Use 2
methods. One is using slicing and other using loops. Both should be
written. So basically make 2 functions for each.
"""


# Method 1:
def palindrome1(my_string: str) -> bool:
    new_string = ""
    for i in my_string[::-1]:
        new_string += i
    return new_string == my_string


def palindrome2(my_string: str) -> bool:
    new_string = my_string[::-1]
    return new_string == my_string


print(palindrome1("abcba"))
print(palindrome2("abcba"))
