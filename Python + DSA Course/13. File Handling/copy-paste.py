""" Want to copy one file into other."""

input_file = input(
    "Enter a file name to copy to: "
)  # You will have use extension of the file as well
output_file = input("Enter a file name to copy from: ")

# Method 1:
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

# Method 2: Best Method
exists = False
try:
    f = open(input_file, "r")
    data = f.read()
    f.close()
    exists = True
except FileNotFoundError:
    print("File does not exists")
except:
    print("Unknown error occured.")
try:
    if exists == True:
        f = open(output_file, "w")
        f.write(data)
        f.close()
except:
    print("Some unkown error has occured.")


# Method 3:
import sys

input_file = input("Enter file to copy from = ")
output_file = input("Enter file to copy to = ")
try:
    f = open(input_file, "r")
    data = f.read()
    f.close()
except FileNotFoundError:
    print("File does not exists")
    sys.exit()  # closes the program.
except:
    print("Some unknown error occurred")
    sys.exit()  # closes the program as soon we get error during reading.

try:
    f = open(output_file, "w")
    f.write(data)
    f.close()
except:
    print("Some unknown error occurred")
