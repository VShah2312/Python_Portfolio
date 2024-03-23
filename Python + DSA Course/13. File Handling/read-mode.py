# Read Mode:
# Method 1:
f = open("hello.txt", "r")
print(type(f))
# Method 1:
data = f.read()  # Reads whole file
print(data)
f.close()  # Good habit to close when you open a file.

# Method 2:
f = open("hello.txt", "r")
for line in f:  # Prints each line.
    # there is /n in file after each line and then /n for print if end not mentioned.
    print(line, end="")
f.close()

# Method 3: Here file has been converted to string in data variable. Thus for loop reads character by character.
f = open("hello.txt", "r")
data = f.read()
for i in data:
    print(i)
f.close()
#
f = open("hello.txt", "r")
d = f.read(3)  # Hel
print(d)
d = f.read(
    5
)  # lo Wo becuase cursor stopped at index 3. Cursor wont reset till we close the file.
print(d)
f.close()


# f = open("hello.txt", "r")
# d = f.read()
# print(d)
# d = f.read()
# print(d) # This will print blank because cursor has stopped at last line.
# f.close()

# Readline:
f = open("hello.txt", "r")
d = f.readline()  # Reads first line. cursor is now at end of line 1.
print(d)
d = f.readline()  # It reads a line from cursor has stopped.
print(d)
f.close()

# Readlines: Gives list of line,
f = open("hello.txt", "r")
d = f.readlines()
print(d)
d = (
    f.readlines()
)  # It will give blank as cursor has stopped at end of the text file from above command.
print(d)
f.close()
