"""
Count capital letters in provided string
"""

a = "PythOn is A GreAT LanngAUGE"
# ASCII for capital is between 65 to 90:
count = 0
for char in a:
    ascii_num = ord(char)
    if ascii_num >= 65 and ascii_num <= 90:
        count += 1
print(count)
count = 0
for char in a:
    if "A" <= char <= "Z":  # Here ASCII value is already converted.
        count += 1
print(count)

# Question: count how many digits are there
a = "PythO232n i232s A 2323GreAT 2323LanngAUGE"
count = 0
for char in a:
    ascii_num = ord(char)
    if ascii_num >= 48 and ascii_num <= 57:
        count += 1
print(count)

count = 0
for char in a:
    if ord(char) >= 48 and ord(char) <= 57:
        count += 1
print(count)

count = 0
for char in a:
    if "0" <= char <= "9":  # Here ASCII value is already converted.
        count += 1
print(count)
