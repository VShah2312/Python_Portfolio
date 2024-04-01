"""
Question 3: Write a function that takes a string as input and returns only vowels in
that string.
"""


def onlyVowels(my_string: str) -> str:
    vowels = [i for i in my_string if i in "aeouiAEIOU"]
    return "".join(vowels)


print(onlyVowels("abcdef"))
print(onlyVowels("A24BKA78EAC%^i"))
print(onlyVowels("12345678"))
