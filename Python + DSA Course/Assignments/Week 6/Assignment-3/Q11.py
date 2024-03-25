"""
Question 11: Print each word of the file in reverse order.
"""


def function(file_name: str, mode="r"):
    f = open(file_name, mode)
    data = f.readlines()
    result = []
    for i in data:
        result.append(i.split())
    for i in result:
        result_2 = ""
        for j in i:
            result_2 = result_2 + j[::-1] + " "
        print(result_2)


function("hello.txt")

# Solution:


def printWordsInReverse(filename: str) -> None:
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            words = line.strip().split()
            reversed_words = [word[::-1] for word in words]
            print(" ".join(reversed_words))
    except FileNotFoundError:
        print("File not found!")


filename = "hello.txt"
printWordsInReverse(filename)
