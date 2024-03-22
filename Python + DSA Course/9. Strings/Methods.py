string = "pyTHOn IS GOOD"

print(string.lower())  # python is good
print(string.upper())  # PYTHON IS GOOD
print(string.title())  # Python Is Good
print(string.capitalize())  # Python is good
print(string.swapcase())  # PYthoN is good
print(
    string.islower()
)  # False Even if we had symbols it would work. It skips symbols and focus on alphabets
print(string.isupper())  # False
print(string.isalpha())  # False Space wont be skipped here.
print(string.isalnum())  # False
print(string.isdigit())  # False
print(string.replace("O", "i"))  # pyTHin IS GiiD
print(string.index("O"))  # first O is on 4
print(string.index("OO"))  # first OO is on 11
# print(string.index("z"))  # ValueError: substring not found
print(string.find("z"))  # -1, no error.
print(string.rfind("O"))  # 12 first value from right

string = "   pyTHOn IS GOOD  "

print(len(string), string.strip(), len(string.strip()))  # 19 pyTHOn IS GOOD 14
# Strip removes whitespace from both left and right
print(len(string), string.lstrip(), len(string.lstrip()))  # 19 pyTHOn IS GOOD   16
# Strip removes whitespace from  left
print(len(string), string.rstrip(), len(string.rstrip()))  # 19    pyTHOn IS GOOD 17
# Strip removes whitespace from  right

print(string.strip("@"))  #    pyTHOn IS GOOD
string = "@@@@ pyTHOn IS GOOD  "
print(string.strip("@"))  # pyTHOn IS GOOD  Strips @

string = "@ @@@ pyTHOn IS GOOD @"
print(string.strip("@"))  # @@@ pyTHOn IS GOOD
