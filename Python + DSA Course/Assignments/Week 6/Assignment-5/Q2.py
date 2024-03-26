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
