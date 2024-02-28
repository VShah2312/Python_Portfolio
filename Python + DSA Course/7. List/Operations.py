a = [45, 32, 11, 100]
b = [75, 25, 1, 100]

# joins two lists.
print(a + b)

# TypeError: can only concatenate list (not "int") to list
# print(a + 3)

# print(a * b)
# TypeError: can't multiply sequence by non-int of type 'list'
print(a * 3)
# [45, 32, 11, 100, 45, 32, 11, 100, 45, 32, 11, 100]
print(a - b)
# TypeError: unsupported operand type(s) for -: 'list' and 'list'
print(a / 3)  # -> ERROR
print(a / 3)  # -> ERROR
print(a / b)  # -> ERROR
print(a - 9)  # -> ERROR
