string = "aerrropllane"

# Creating list of 0 with length 26
char_hash = [0] * 26
# Pre-store:
for char in string:
    index = ord(char) - 97
    char_hash[index] += 1

print(char_hash)
char = input("Enter char to count: ")
print(char_hash[ord(char) - 97])
