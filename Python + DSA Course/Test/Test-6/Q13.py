"""
Question 13: Write a program to get/print the number of characters, words, spaces
and lines in a file.
"""

# Count lines:
f = open("hello.txt", "r")
data = f.readlines()
print(f"Number of lines: {len(data)}")
f.close()

# Count number of words:
f = open("hello.txt", "r")
data_1 = f.read()
list_1 = data_1.split()
print(f"Number of words: {len(data_1.split())}")
f.close()

# Count number of char:
f = open("hello.txt", "r")
data_1 = f.read()
my_list = list(data_1)
print(f"Number of characters: {len(my_list)}")
f.close()

# Count number of spaces:
f = open("hello.txt", "r")
data_1 = f.read()
my_list = list(data_1)
char_count = {char: data_1.count(char) for char in data_1}
print(char_count)
print(f"Number of spaces: {char_count.get(' ', 'No spaces. ')}")
f.close()
