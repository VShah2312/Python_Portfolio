# Read Mode Questions:

# my_string= "Hello world.\n This is python."
# Alternate way: Docs string
my_string = """Hello world.
This is python."""
print(my_string)

# Question 1: How many lines are there in the files:
f = open("hello.txt", "r")
lines = f.readlines()
print(len(lines))
f.close()

# Question 2: How many words are there in the files:
f = open("hello.txt", "r")
# Default for split is white space( space, enter, tab )
data = f.read()
words = data.split()
print(len(words))
f.close()

# Question 3: How many words in each line?
f = open("hello.txt", "r")
lines = f.readlines()
for line in lines:
    print(len(line.split()))
f.close()

# OR

f = open("hello.txt", "r")
for line in f:
    print(len(line.split()))
f.close()

# Question 3: How many char in each words in each line?
# Here we get one extra char (i.e \n)
f = open("hello.txt", "r")
lines = f.readlines()
for line in lines:
    print(len(line.strip()))
f.close()
