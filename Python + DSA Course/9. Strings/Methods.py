string = "pyTHOn IS GOOD"

print(string.lower())  # python is good
print(string.upper())  # PYTHON IS GOOD
print(string.title())  # Python Is Good
print(string.capitalize())  # Python is good
print(string.swapcase())  # PYthoN is good
print(
    string.islower()
)  # False Even if we had symbols it would work. It skipps symbols and focus on alphabets
print(string.isupper())  # False
print(string.isalpha())  # False Space wont be skipped here.
print(string.isalnum())  # False
print(string.isdigit())  # False
