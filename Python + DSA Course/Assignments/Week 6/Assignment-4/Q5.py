"""
Question 5: Write a Python program to generate 26 text files named A.txt, B.txt,
and so on up to Z.txt. There should be no content in any of them. You just
need to create these files. (Search for how to create a file on google. Also
you can use Write mode to create a file).
"""

import string


# solution:
def generateFiles():
    try:
        for letter in string.ascii_uppercase:
            filename = letter + ".txt"
            with open(filename, "w") as file:
                pass
        print("Files created successfully.")
    except IOError:
        print("Error: An I/O error occurred.")


generateFiles()
