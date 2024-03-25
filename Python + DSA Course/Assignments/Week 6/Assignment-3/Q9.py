"""
Question 9: There is a file having numbers in each line of that file. Calculate the
total of all numbers.
"""


def function(file_name: str, mode="r"):
    f = open(file_name, mode)
    data = f.readlines()
    sum = 0
    for line in data:
        sum += int(line)
    return sum


print(function("hello1.txt"))


# Solution:
def calculateTotal(filename: str) -> int:
    try:
        # Shortcut
        # calculate = sum(list(map(int, f.read().split())))
        # return calculate
        file = open(filename, "r")
        total = 0
        for line in file:
            total += int(line.strip())
        file.close()
        return total
    except FileNotFoundError:
        print("File not found!")
        return -1  # Return -1 to indicate an error


filename = "hello.txt"
total = calculateTotal(filename)
if total != -1:
    print(f"Total = {total}")
