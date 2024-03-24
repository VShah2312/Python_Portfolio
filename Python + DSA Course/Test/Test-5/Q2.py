"""
Question 2: Write a program to rotate the characters in a string by a given number
of positions. For example, given the input "abcdef" and rotation of 2, the
output should be "efabcd".
Ask string and rotation from the user.
"""


def rotation(string: str, rotation: int) -> str:
    my_list = list(string)
    result = str()
    for i in range(rotation):
        result += my_list.pop()
    return result[::-1] + "".join(my_list)


string = "abcdef"
print(rotation(string, 2))


# Solution:
def rotationOfString(string: str, rotation: int) -> str:
    # We will keep removing last character from the end
    # and put it to the front. This is one rotation
    for _ in range(rotation):
        """
        string[-1] means last character
        string[:-1] means from start to end-1
        """
        string = string[-1] + string[:-1]
    return string


s = "abcdef"
result = rotationOfString(s, 2)

print(result)
