"""
Question 10: Print each line of the file in reverse order.
"""


def function(file_name: str, mode="r"):
    f = open(file_name, mode)
    lines = f.readlines()
    for line in lines:
        result = line.split()
        print(" ".join(result[::-1]))


function("hello.txt")


def printLines(filename: str) -> None:
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            words = line.strip().split()
            reversed_words = words[::-1]
            reversed_line = " ".join(reversed_words)
            print(reversed_line)
    except FileNotFoundError:
        print("File not found!")


filename = "hello.txt"
printLines(filename)
