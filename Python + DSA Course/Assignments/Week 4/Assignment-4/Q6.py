"""
Question 6: Write a function which accepts a String and another string (which will
be a single character) as a parameter. Join that string along with that
character.
"""


def joinString(string: str, char: str) -> str:
    result = string.split()
    return char.join(result)


user_input = input("Enter a string: ")
char = input("Enter a character: ")
print(joinString(user_input, char))


# Solution:
def joinString_solution(string: str, char: str) -> str:
    words = string.split()
    result = char.join(i for i in words)
    return result

    # Single line
    # return char.join(i for i in string.split())


r = joinString_solution("hello world", "%")
print(r)
