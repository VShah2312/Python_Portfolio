"""
Question 7: There is a file (any random file) having sentences in it. Create a new file
result.txt having each sentence in a reverse order.
"""


def function(file_name: str, file_name_result: str, mode="r"):
    exists = False
    try:
        f = open(file_name, mode)
        lines = f.readlines()
        result_1 = lines[::-1]
        f.close()
        exists = True
    except:
        print("Some Error has occured in read.")
    try:
        if exists == True:
            f = open(file_name_result, "w")
            result = [i.strip() for i in result_1]
            f.write("\n".join(result))
            f.close()
    except:
        print("Some Error has occured in write.")


function("hello.txt", "hello_result_2.txt")

# Solution:


def reverseLines(input_file: str, output_file: str) -> None:
    try:
        with open(input_file, "r") as file_in:
            lines = file_in.readlines()

        with open(output_file, "w") as file_out:
            for line in lines[::-1]:
                file_out.write(line)

    except FileNotFoundError:
        print("Error: Input file not found.")
    except IOError:
        print("Error: An I/O error occurred.")


reverseLines("input.txt", "result.txt")
