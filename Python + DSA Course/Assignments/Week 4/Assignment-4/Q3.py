"""
Question 3: Write a function which accepts a String as a parameter and return the
reversed words as a String.
"""


def reverseWords(my_string: str) -> str:
    result = my_string.split()
    return " ".join(result[::-1])


print(reverseWords("python is great"))
print(reverseWords("we live in delhi.  there is no pollution,very clean city"))


# Solution:
def reverseWords(string: str) -> str:
    words = string.split()
    words.reverse()
    result = " ".join(i for i in words)
    return result

    # Shortcut
    # return " ".join(i for i in reversed(string.split()))


print(reverseWords("python is great"))
