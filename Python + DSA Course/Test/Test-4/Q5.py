"""
Question 5: Ask a string from user. Replace all the space characters with “-”.
Do not use replace() method.
"""


def replaceSpace(my_string: str) -> str:
    words = my_string.split()
    result = "-".join(words)
    return result


my_string = "python is a great language"
print(replaceSpace(my_string))


# Solution:
def replaceSpaces(string):
    result = ""
    for char in string:
        if char == " ":
            result += "-"
        else:
            result += char
    return result


user_string = input("Enter a string: ")

r = replaceSpaces(user_string)

print(r)
