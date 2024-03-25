"""
Question 8: Aditi has used a text editing software to type some text. After saving
the article as WORDS.TXT, she realized that she has wrongly typed
alphabet J in place of alphabet I everywhere in the article.
Write a function definition for JTOI() in Python that would display the
corrected version of entire content of the file WORDS.TXT with all the
alphabets " J" to be displayed as an alphabet "I" on screen.
"""


def JTOI(file_name: str, mode="r"):
    f = open(file_name, mode)
    data = f.read()
    data_2 = data.replace("j", "i")
    data_3 = data_2.replace("J", "I")
    return data_3


print(JTOI("word.txt"))


# Solution:
def JTOI(filename):
    try:
        file = open(filename, "r")
        data = file.read()
        corrected_data = data.replace("J", "I")
        print(corrected_data)
        file.close()
    except FileNotFoundError:
        print("File not found!")


JTOI("hello.TXT")
