"""
Question 1: Given a list of strings, concatenate them into a single string separated
by spaces. For example, given the input ["Hello","World","Python"]
output should be "Hello World Python".
Don’t use the JOIN function.
"""


def concat(my_list: list[str]) -> str:
    result = str()
    for i in my_list:
        result = result + i + " "
    return result


my_list = ["Hello", "World", "Python"]
print(concat(my_list))

# Solution:
from typing import List


def joinWords(words: List[str]) -> str:
    result = ""
    for word in words:
        result += word
        result += " "
    return result


my_words = ["Hello", "World", "Python"]

s = joinWords(my_words)
print(s)
