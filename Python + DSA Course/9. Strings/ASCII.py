"""
ASCII: All the keys on keyboard has a numeric value for CPU to understand. 
For capital and lower case its different. 
"""

my_string = "a"
print(ord(my_string))
my_string = "b"
print(ord(my_string))

my_string = "python is a great language"
count = 0
for char in my_string:
    if char == "e" or char == "E":
        count += 1

print(count)

# Alternate method:
for char in my_string:
    ascii_num = ord(char)
    if ascii_num == 101 or ascii_num == 69:  # 101 for 'e' and 69 for 'E'
        count += 1
print(count)
