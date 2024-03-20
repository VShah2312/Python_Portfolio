"""
Question 6: vWrite a python program to ask a string from user. Then count the
number of vowels and number of consonants in that string.
"""


def countVowel(str) -> str:
    vowel = 0
    consonant = 0
    for char in str:
        if "a" <= char.lower() <= "z":
            if char.lower() in ["o", "u", "i", "e", "a"]:
                vowel += 1
            else:
                consonant += 1
    return f"vowel = {vowel} and consonant= {consonant}"


print(countVowel("VrunDA Ch@rm6"))

# Solution:
