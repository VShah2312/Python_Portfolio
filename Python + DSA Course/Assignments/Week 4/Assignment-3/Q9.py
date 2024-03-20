"""
Question 9: Write a python program to only print second half of the string. Ask
string from user.
"""


def secondHalf(my_str) -> str:
    length = len(my_str) // 2
    return my_str[-length::]


print(secondHalf("delhi"))
print(secondHalf("aeroplane"))
print(secondHalf("pavbhaji"))
