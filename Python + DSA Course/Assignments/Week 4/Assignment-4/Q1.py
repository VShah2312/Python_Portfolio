"""
Question 1: Ask a string from user. If the length of string is odd, then change all the
capital letters to small and vice versa, but if the length of string is even,
reverse the string. Do this using a function and return the output.
"""


def changeString(my_string: str):
    if len(my_string) % 2 == 0:
        # If you pass a string to reversed(), you get an iterator that yields characters in reverse order:
        # So you need to use join
        result = "".join(reversed(my_string))  # OR my_string[::-1]
        return result
    else:
        return my_string.swapcase()


print(changeString("AEroPLane"))
print(changeString("AEroPLanes"))
