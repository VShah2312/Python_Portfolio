# Question: How many words are there in the file:
def function(file_name: str) -> int:
    f = open(file_name, "r")
    data = f.read()
    # Default for split is white space( space, enter, tab )
    words = data.split()
    f.close()
    return len(words)


print(function("hello.txt"))


# Question: How many vowels are there in the file:
def function_2(file_name: str) -> int:
    count = 0
    f = open(file_name, "r")
    data = f.read()
    for char in data:
        if char.lower() in "aeiou":
            count += 1
    return count


print(function_2("hello.txt"))


# Question: How many digits are there in the file:
def function_3(file_name: str) -> int:
    count = 0
    f = open(file_name, "r")
    data = f.read()
    for char in data:
        if char.isdigit():
            count += 1
    return count


print(function_3("hello.txt"))


# Question: Find sum of all digits are there in the file:
def function_4(file_name: str) -> int:
    sum = 0
    f = open(file_name, "r")
    data = f.read()
    for char in data:
        if char.isdigit():
            sum += int(char)
    return sum


print(function_4("hello.txt"))


# Question: File has all numbers:
# Method 1:
def function_5(file_name: str) -> int:
    sum = 0
    f = open(file_name, "r")
    data = f.read()
    for num in data.split():
        print(num)
        sum += int(num)
    f.close()
    return sum


print(function_5("hello.txt"))

# Method 2:


def function_5_2(file_name: str) -> int:
    f = open(file_name, "r")
    sum = 0
    numbers = f.readlines()
    for number in numbers:
        number = number.strip()
        sum = sum + int(number)
    f.close()
    return sum


print(function_5_2("hello.txt"))


# Method 3:
f = open("hello.txt", "r")
data = f.read().split()
sum = 0
for i in data:
    sum += int(i)

print(sum)
f.close()
