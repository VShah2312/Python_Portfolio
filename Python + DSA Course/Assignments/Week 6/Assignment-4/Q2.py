"""
Question 2: here is a file named numbers.txt and the content is given below. Content (numbers.txt)
34
67
98
11
-87
100
Create another file named numbers_result.txt. It should have the following content in it based on numbers.txt.
34 Even
67 Odd
98 Even
11 Odd
-87 Odd
100 Even
"""


def function(file_name: str, file_name_result: str, mode="r"):
    exists = False
    try:
        f = open(file_name, mode)
        lines = f.readlines()
        my_dict = {}
        for line in lines:
            if int(line.strip()) % 2 == 0:
                my_dict[line.strip()] = "Even"
            else:
                my_dict[line.strip()] = "Odd"

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


function("numbers.txt", "numbers_result.txt")


# Solution :
def numbersOddEven(input_file: str, output_file: str):
    try:
        with open(input_file, "r") as file_in:
            with open(output_file, "w") as file_out:
                for line in file_in:
                    number = int(line.strip())
                    if number % 2 == 0:
                        file_out.write(f"{number} Even\n")
                    else:
                        file_out.write(f"{number} Odd\n")
        print(f"Content written to '{output_file}' successfully.")
    except FileNotFoundError:
        print("Error: One or both files not found.")
    except IOError:
        print("Error: An I/O error occurred.")


numbersOddEven("numbers.txt", "numbers_result.txt")
