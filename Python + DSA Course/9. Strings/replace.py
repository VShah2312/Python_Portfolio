a = "delhi is clean city"

r = a.replace("i", "z")
print(r)

# Replace i with z without using replace function:
result = a.split()
print(result)

r = []
for words in result:  # you dont need for loop here.
    r1 = ["z" if i == "i" else i for i in words]
    r.append("".join(r1))
print(" ".join(r))

# OR
# result = a.split()
result = list(a)
print(result)

r1 = ["z" if i == "i" else i for i in result]
# r1= [ch if ch!="i" else "z" for ch in char]
r = "".join(r1)  # Here list also has spaces. So we dont need to add it.

print(r)
# OR

result = "".join(["z" if i == "i" else i for i in list(a)])
print(result)


# OR
def replaceChar(string: str) -> str:
    new_string: str = str()
    for char in string:
        if char.lower() == "i":
            new_string += "z"
        else:
            new_string += char
    return new_string


r = replaceChar(a)
print(r)
