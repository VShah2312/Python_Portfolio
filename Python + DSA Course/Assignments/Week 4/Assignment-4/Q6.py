"""
Question 6: Write a function which accepts a String and another string (which will
be a single character) as a parameter. Join that string along with that
character.
"""


def joinReverse(string: str, char: str) -> str:
    result = string.split()
    return char.join(result[::-1])


user_input = input("Enter a string: ")
char = input("Enter a character: ")
print(joinReverse(user_input, char))
