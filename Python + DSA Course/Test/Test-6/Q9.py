"""
Question 9: Given a string of size n, write functions to perform following operations
on string:
Left (Or anticlockwise) rotate the given string by d elements (where d
<= n).
Right (Or clockwise) rotate the given string by d elements (where d <=
n).
"""


def rotation(my_string: str, d: int) -> str:
    left_newstring = my_string[d:] + my_string[:d]
    right_newstring = my_string[-d::] + my_string[:-d]
    print(f"Left Rotation: {left_newstring}")
    print(f"Right Rotation: {right_newstring}")


my_string = input("Enter string: ")
d = int(input("Enter rotation: "))
rotation(my_string, d)
