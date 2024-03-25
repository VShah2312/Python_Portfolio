"""
Question 1: Make a function which takes filename as a parameter. Return the
number of words present in that file.
"""


def function(file_name: str, mode="r"):
    f = open(file_name, mode)
    data = f.read()
    words = data.split()
    f.close()
    return len(words)


print(function("hello.txt"))

# Solution:


def countWords(filename: str) -> int:
    try:
        file = open(filename, "r")
        data = file.read()
        word_count = len(data.split())
        file.close()
        return word_count
    except FileNotFoundError:
        print("File not found!")
        return -1  # Return -1 to show user there is an error


file_name = "hello.txt"
word_count = countWords(file_name)
if word_count != -1:
    print(f"Number of words in {file_name} = {word_count}")
