# String -> List
my_string = "python is great."
r = list(my_string)
# Give all character of string as an list element including spaces and symbols.
print(r)

# List -> String
my_list = [2, 5, 1, 8, 9, 8]
result = str(my_list)  # Output: "[2, 5,1,8,9,8]"
print(
    result
)  # Output: "[2, 5,1,8,9,8]" so result[0]= "["", result[1]= "2", result[2]=","
result = "".join(str(i) for i in my_list)  # 251898
# Space is what we are going to use for joining. And basic requirement is to join is to have strings.
print(result)


my_list = ["a", "y", "u", "i"]
print(" ".join(str(i) for i in my_list))  # a y u i 1 2 4
print(" ".join(my_list))  # a y u i
# We can do above method if we know all elements of the lists are string.
# If you are not sure its better to convert to string.
