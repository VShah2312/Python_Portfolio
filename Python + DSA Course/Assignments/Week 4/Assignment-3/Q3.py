"""
Question 3: Write a Python program to check whether an element exists within a
tuple. Ask something from user, if that exists in tuple, then print “YES” else
print “NO”.
"""


def function(my_tuple, num: int) -> str:
    if num in my_tuple:
        return "Yes"
    return "No"


my_tuple = (56, 2, 0, 56, 34, 76, 34, 45, 1, 2, 3)
print(function(my_tuple, 8))


# Solution:
def elementExistsInTuple(element, t):
    return element in t


my_tuple = (1, 2, 3, 4, 5)

e = int(input("Enter an element = "))

if elementExistsInTuple(e, my_tuple):
    print("YES")
else:
    print("NO")
