"""
Question 6:There is a file having sentences in it. Create a new file result.txt having
the same sentence as it is but also number of vowels written beside each
line.
"""


def function(file_name: str, file_name_result: str, mode="r"):
    exists = False
    try:
        f = open(file_name, mode)
        lines = f.readlines()
        my_dict = {}
        for line in lines:
            count = 0
            for i in line:
                if i in "aeiouAEIOU":
                    count += 1
            my_dict[line.strip()] = count
        f.close()
        exists = True
    except:
        print("Some Error has occured in read.")
    try:
        if exists == True:
            f = open(file_name_result, "w")
            for k, v in my_dict.items():
                result = str(k) + " " + str(v) + "\n"
                f.write(result)
            f.close()
    except:
        print("Some Error has occured in write.")


function("hello.txt", "hello_result.txt")


# Solution:
def countVowels(sentence: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count


def addVowelCount(input_file: str, output_file: str) -> None:
    try:
        with open(input_file, "r") as file_in:
            lines = file_in.readlines()

        with open(output_file, "w") as file_out:
            for line in lines:
                line = line.strip()
                vowel_count = countVowels(line)
                file_out.write(f"{line} {vowel_count}\n")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except IOError:
        print("Error: An I/O error occurred.")


addVowelCount("input.txt", "result.txt")
