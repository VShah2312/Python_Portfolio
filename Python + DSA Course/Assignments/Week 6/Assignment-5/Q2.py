"""
Question 2: Create a function named arrangeChars which takes a string as a
parameter. Now return a string with max frequency chars at start.
"""


def arrangeChars(my_string: str) -> str:
    result = sorted(
        my_string, key=lambda x: (my_string.count(x), -ord(x)), reverse=True
    )
    # Here if characters have same frequency it will sort them based on ASCII value (character with lower ASCII values will go first)
    # If we didnt have reverse=True, we would use only ord(x)
    return "".join(result)


print(arrangeChars("aaeroplanee"))
print(arrangeChars("heelllllooo"))


# Solution:
def arrangeChars(string: str) -> str:
    characters_count = {}
    for ch in string:
        characters_count[ch] = characters_count.get(ch, 0) + 1
    characters_count = dict(
        sorted(characters_count.items(), key=lambda x: x[1], reverse=True)
    )
    result = ""
    for char, count in characters_count.items():
        result += char * count
    return result


print(arrangeChars("aaeroplane"))
