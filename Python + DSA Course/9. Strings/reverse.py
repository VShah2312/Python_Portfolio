my_string = "python is great"

for words in my_string.split():
    print(words[::-1])

# OR
result = [words[::-1] for words in my_string.split()]
print(" ".join(result))
