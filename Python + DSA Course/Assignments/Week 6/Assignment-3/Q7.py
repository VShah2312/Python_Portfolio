"""
Question 7: Make a function which takes filename as a parameter. Return the count
of uppercase characters in that file.
"""


def function(file_name: str, mode="r"):
    f = open(file_name, mode)
    data = f.read()
    count = 0
    for i in list(data):
        if i.isupper():
            count += 1
    return count


print(function("hello.txt"))


# Solution:
def countUppercaseCharacters(filename: str) -> int:
    try:
        file = open(filename, "r")
        data = file.read()
        file.close()
        # count = sum(1 for char in content if char.isupper())  # Shortcut
        count = 0
        for char in data:
            if char.isupper():
                count += 1
        return count
    except FileNotFoundError:
        print("File not found!")
        return -1  # Return -1 to indicate an error


filename = "hello.txt"
uppercase_count = countUppercaseCharacters(filename)
if uppercase_count != -1:
    print(f"Count of uppercase characters = {uppercase_count}")
