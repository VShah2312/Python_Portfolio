"""
Question 1:  Make a function named copyFileContent which takes 2 filenames
(filename1, filename2) as an argument. Copy the content of filename1 to
filename2.
"""


def copyFileContent(filename1: str, filename2: str):
    exists = False
    try:
        f = open(filename1, "r")
        data = f.read()
        f.close()
        exists = True
    except FileNotFoundError:
        print("File does not exists")
    except:
        print("Unknown error occured.")
    try:
        if exists == True:
            f = open(filename2, "w")
            f.write(data)
            f.close()
    except:
        print("Some unkown error has occured.")


print(copyFileContent("numbers.txt", "numbers_copy.txt"))
