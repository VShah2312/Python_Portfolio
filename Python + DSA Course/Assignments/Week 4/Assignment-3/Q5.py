"""
Question 5: Write a Python program to check if a string has at least one letter and
one number. If it has at least one letter and one number then print YES else
print NO.

Couldn't do it on my own.
"""


def checkNumberAndLetter(my_string: str) -> bool:
    isLetter = False
    isNumber = False

    # Method 1: Basically ch has a number or letter it will change bool to True and
    # then if it find more of letter of number it will set it to True again.
    """
    for ch in my_string:
        if ch.isdigit():
            isNumber = True
        elif ch.isalpha():
            isLetter = True

    return isLetter and isNumber
    """

    for ch in my_string:
        ascii_code = ord(ch)
        if ascii_code >= 48 and ascii_code <= 57:
            isNumber = True
        elif (ascii_code >= 65 and ascii_code <= 90) or (
            ascii_code >= 97 or ascii_code <= 122
        ):
            isLetter = True

    return isLetter and isNumber


print(checkNumberAndLetter("abc#$#1d"))
