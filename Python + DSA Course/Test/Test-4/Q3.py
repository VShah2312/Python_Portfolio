"""
Question 3: Python Program to remove all duplicates from a given string.
"""


def removeDuplicate(string: str) -> str:
    result = ""
    for i in string:
        if i not in result:
            result += i
    return result


my_string = input("Enter a string: ")
print(removeDuplicate(my_string))


# Solution:
def removeDuplicates(string):
    result = ""

    for char in string:
        if char not in result:
            result += char

    return result


string = "hheeelllooo"
print(removeDuplicates(string))
