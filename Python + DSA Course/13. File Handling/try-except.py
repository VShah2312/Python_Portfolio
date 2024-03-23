# In read mode file has to exist:

f = open("xyz.txt", "r")
data = f.read()
print(data)
f.close()
# FileNotFoundError: [Errno 2] No such file or directory: 'xyz.txt'c


try:
    f = open("xyz.txt", "r")
    data = f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print("File does not exists")
except:
    print("Some error occurred")
