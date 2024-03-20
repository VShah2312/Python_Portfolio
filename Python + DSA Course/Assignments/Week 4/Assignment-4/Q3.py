"""
Question 3: Write a function which accepts a String as a parameter and return the
reversed words as a String.
"""


def reverseWords(my_string: str) -> str:
    result = [i for i in my_string.split()]
    return " ".join(result[::-1])


print(reverseWords("python is great"))
print(reverseWords("we live in delhi.  there is no pollution,very clean city"))
