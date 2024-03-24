"""
Question 3: Write a Python program to convert a given string to all uppercase if it
contains at least 2 uppercase characters in the first 4 characters.
Input: pyTHon
Output: PYTHON
Input: helLo
Output: helLo
Input: gOOD
Output: GOOD
"""


def case(string: str):
    upper = 0
    for i in string[::4]:
        if i.isupper():
            upper += 1
    if upper >= 2:
        return string.upper()
    return string


my_string = "pyTHon"
print(case(my_string))
my_string = "helLO"
print(case(my_string))
my_string = "gOOD"
print(case(my_string))

# Solution: def convertToUppercase(s: str) -> str:
upper_count = sum(1 for c in s[:4] if c.isupper())
    if upper_count >= 2:
        return s.upper()
    return s


result = convertToUppercase("HelLo")
print(result)

result = convertToUppercase("Helo")
print(result)

def convertToUppercase(s: str):
    upper_count = 0
    for c in s[:4]:
        if c.isupper():
            upper_count += 1
    if upper_count >= 2:
        return s.upper()
    return s


result = convertToUppercase("HelLo")
print(result)

result = convertToUppercase("Helo")
print(result)