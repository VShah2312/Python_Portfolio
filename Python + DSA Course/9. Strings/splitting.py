my_string = "python is a great language"
result = my_string.split()
print(result)
my_string = "aeroplane"
result = my_string.split("o")
print(result)

# Question:
my_string = "python is a great language"
result = my_string.split()
result = result[::-1]
s = " ".join(result)
print(s)

# Question: Ask a string from a user and reverse the wods it
my_string = input("Enter a string: ")
result = my_string.split()
result = result[::-1]
s = " ".join(result)
# As result is a list and its iterable.  So we can use it directly too.
print(s)

# Question: Ask a string from user and reverse the characters of each word
my_string = input("Enter a string: ")
result = my_string.split()
result_2 = []
for word in result:
    result_2.append(word[::-1])
print(result_2)
s = " ".join(result_2)
print(s)

# OR

my_string = input("Enter a string: ")
words = my_string.split()
s = " ".join(i[::-1] for i in words)
print(s)
