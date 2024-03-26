"""
Question 4: Write a Python program to read last n lines of a file. Ask n from user
and read any file you want to. If n is greater than number of lines actually
present in that file, show output like “Not Enough Lines”.
"""


def function(num: int):
    try:

        f = open("numbers.txt", "r")
        data = f.readlines()
        f.close()
        print(len(data))
        assert len(data) >= num, "Not enough lines."
        print("".join(data[-num::]))
    except Exception as e:
        print(e)
    except:
        print("Some error has occured.")


function(2)
function(12)
function(6)
