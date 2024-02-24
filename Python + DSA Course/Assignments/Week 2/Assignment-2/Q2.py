""" 
Question 2: Implement a function that takes two parameters, base and exponent,
and returns the result of raising the base to the power of the exponent.
"""


def exponent(b: int = None, exp: int = None) -> int:
    if b == None or exp == None:
        return None
    return b**exp


print(exponent(2, 4))
print(exponent())
