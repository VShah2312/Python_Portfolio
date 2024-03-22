# With keyword: does the clean up for you.

with open("hello.txt", "r") as f:
    data = f.read()
    print(data)

# data= f.read() this will throw error as file will be close before existing with block
print("Done ")

# Copying with with block:
# Open close, open close
with open("hello.txt", "r") as f:
    data = f.read()
with open("hello_1.txt", "w") as f:
    f.write(data)

# Open open close close
with open("hello.txt", "r") as f1:
    data = f1.read()
    with open("hello_1.txt", "w") as f2:
        f2.write(data)

# f in read mode, f1 in write mode
with open("hello.txt", "r") as f, open("hello1.txt", "w") as f1:
    data = f.read()
    f1.write(data)
    # f1.write(f.read())
