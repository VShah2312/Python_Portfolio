a = [56, 56, 69, 1, 2]

# a.copy is excuted and then result is going into sort() but we dont get results as sort returns None.
# b = a.copy().sort()
# print(b)

# a.copy will return [56, 56, 69, 1, 2] and then pop() from it.
b = a.copy().pop()
print(b)
