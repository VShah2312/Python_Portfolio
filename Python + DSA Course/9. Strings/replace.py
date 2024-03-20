a = "delhi is clean city"

r = a.replace("i", "z")
print(r)

# Replace i with z without using replace function:
result = a.split()
print(result)

r = []
for words in result:
    r1 = ["z" if i == "i" else i for i in words]
    r.append("".join(r1))
print(" ".join(r))

# OR
# result = a.split()
result = list(a)
print(result)

r = ""
for char in result:
    r1 = ["z" if i == "i" else i for i in char]
    r += "".join(r1)

print(r)
