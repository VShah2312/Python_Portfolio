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


# Solution:
def copyFileContent(filename1: str, filename2: str) -> None:
    try:
        with open(filename1, "r") as file1:
            content = file1.read()
            with open(filename2, "w") as file2:
                file2.write(content)
        print(f"Content copied from '{filename1}' to '{filename2}' successfully.")
    except FileNotFoundError:
        print("Error: One or both files not found.")
    except IOError:
        print("Error: An I/O error occurred.")


# Change the filename as per your requirement
copyFileContent("source.txt", "destination.txt")
