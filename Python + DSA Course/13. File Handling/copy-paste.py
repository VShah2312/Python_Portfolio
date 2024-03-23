""" Want to copy one file into other."""

input_file = input(
    "Enter a file name to copy to: "
)  # You will have use extension of the file as well
output_file = input("Enter a file name to copy from: ")

try:
    f = open(input_file, "r")
    data = f.read()
    f.close()
    # Option 1:
    f = open(output_file, "w")
    f.write(data)
    f.close()
except FileNotFoundError:
    print("File does not exists")
except:
    print("Unknown error occured.")


# Code :
import sys

input_file = input("Enter file to copy from = ")
output_file = input("Enter file to copy to = ")
try:
    f = open(input_file, "r")
    data = f.read()
    f.close()
except FileNotFoundError:
    print("File does not exists")
    sys.exit()
except:
    print("Some unknown error occurred")
    sys.exit()

try:
    f = open(output_file, "w")
    f.write(data)
    f.close()
except:
    print("Some unknown error occurred")
# ...
