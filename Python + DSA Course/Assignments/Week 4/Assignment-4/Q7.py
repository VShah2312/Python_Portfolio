"""
Question 7: Write a function which accepts a String and another string 
(which will be a single character) as a parameter. 
Join that string along with that character but in reverse.
"""


def joinReverse(string: str, char: str) -> str:
    result = string.split()
    return char.join(result[::-1])


user_input = input("Enter a string: ")
char = input("Enter a character: ")
print(joinReverse(user_input, char))


# Solution:
def joinStringReverse(string: str, char: str) -> str:
    words = string.split()
    words.reverse()
    result = char.join(i for i in words)
    return result

    # Single line
    # return char.join(i for i in string.split()[::-1])


r = joinStringReverse("hello world", "%")
print(r)
