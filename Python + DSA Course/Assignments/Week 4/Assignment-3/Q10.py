"""
Question 10: Ask a string from user. Print how the count of alphabets (a-z or A-Z) in
that string.
"""


def countAlphabets(my_str) -> int:
    count = 0
    for char in my_str:
        if "a" <= char.lower() <= "z":
            count += 1
    return count


print(countAlphabets("@er0plane"))
