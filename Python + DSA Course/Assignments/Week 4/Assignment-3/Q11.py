"""
Question 11: Ask a string from user. Print how many spaces are there in that string.
"""


def space(my_string) -> int:
    count = 0
    for char in my_string:
        if char == " ":
            count += 1
    return count


print(space("python is geat"))
