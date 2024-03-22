"""
Question 6: Make a password strength function. It will accept a string from user.
    Return True if it is a strong password.
    Strong password has these characteristics.
    Minimum 8 character
    Minimum 1 uppercase alphabet
    Minimum 1 lowercase alphabet
    Contains at least 1 special symbol (any symbol)
    Minimum 1 digit
"""


def passwordCheck(string: str) -> bool:
    digit = False
    upper = False
    lower = False
    symbol = False
    if len(string) >= 8:
        for i in list(string):
            if i.isdigit():
                digit = True
            if i.isupper():
                upper = True
            if i.lower():
                lower = True
            if i in "`! @#$%^&*()_-+={[}]|\\:;\"'<,>.?/":
                symbol = True
    return digit and upper and lower and symbol


string = input("Enter a password: ")
print(passwordCheck(string))
