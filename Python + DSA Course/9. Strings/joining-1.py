"""
Question: Ask a string from user. Replace all vowels with 'z'
"""

# Method 1:
user_input = input("Enter a input: ")
user_list = list(user_input)
for index, char in enumerate(user_list):
    if char in ["a", "e", "i", "o", "u"]:
        user_list[index] = "z"

print("".join(str(i) for i in user_list))

# Method 2:
# Solution with ternary:

user_input = input("Enter a input: ")
vowels = ["a", "e", "i", "o", "u"]
new_string = "".join([i if i not in vowels else "z" for i in user_input])
print(new_string)

# Method 3:

# Keep in mind:
a = ""
a += "xyz"  # This is allowed as we are creating new object here where we concated ""+ "xyz"
print(a)

str = ""
for char in user_input:
    if char in "aieou":
        str += "z"
    else:
        str += char

print(str)
