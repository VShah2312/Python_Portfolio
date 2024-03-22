a = [56, 56, 69, 1, 2]

# a.copy is excuted and then result is going into sort() but we dont get results as sort returns None.
# b = a.copy().sort()
# print(b)

# a.copy will return [56, 56, 69, 1, 2] and then pop() from it.
b = a.copy().pop()
print(b)


# Example 2:
a = [43, 54, 32, 1, 11, 23, 45]

answer = sorted(a).index(54) + 5
print(answer)
