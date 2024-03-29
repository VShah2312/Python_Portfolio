"""
Question 1: Create a function named oddCharacters which takes a string as a
parameter. Now return a list of characters which appears odd times in that
string.
"""


def oddCharacters(my_string: str) -> list:
    result = [i for i in my_string if my_string.count(i) % 2 != 0]
    result_2 = []
    for i in result:
        if i not in result_2:
            result_2.append(i)
    return result_2


print(oddCharacters("hello"))
print(oddCharacters("aeroplane"))

# Solution:
from typing import List


def oddCharacters(string: str) -> List[str]:
    characters_count = {}
    for ch in string:
        characters_count[ch] = characters_count.get(ch, 0) + 1
    result = []
    for char, count in characters_count.items():
        if count % 2 == 1:
            result.append(char)
    return result


print(oddCharacters("aeroplane"))
