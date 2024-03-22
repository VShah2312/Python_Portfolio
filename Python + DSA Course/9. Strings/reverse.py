my_string = "python is great"
result = []

for words in my_string.split():
    result.append(words[::-1])
print(" ".join(result))

# OR
result = [words[::-1] for words in my_string.split()]
print(" ".join(result))
