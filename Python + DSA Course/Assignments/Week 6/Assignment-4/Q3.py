"""
Question 3: Create a function named multiplication which takes 2 parameter which
are filename and a number. Write the multiplication table of that number in that filename.
Content in filename after running the code, lets suppose number = 5.
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
...
5 x 10 = 50
"""


def function(file_name: str, num: int, mode="w"):
    try:
        f = open(file_name, mode)
        list = [f"{num} x {i} = {num *i}" for i in range(1, 11)]
        list_2 = "\n".join(list)
        f.write(list_2)
        f.close()
    except:
        print("Some Error has occured in write.")


function("multiplication.txt", 5)


# solution:
def multiplication(filename: str, number: int) -> None:
    try:
        with open(filename, "w") as file:
            for i in range(1, 11):
                result = number * i
                file.write(f"{number} x {i} = {result}\n")
        print(
            f"Multiplication table of {number} is written to '{filename}' successfully."
        )
    except IOError:
        print("Error: An I/O error occurred.")


multiplication("multiplication_table.txt", 5)
