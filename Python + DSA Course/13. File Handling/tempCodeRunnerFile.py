def function_4(file_name: str) -> int:
    sum = 0
    f = open(file_name, "r")
    data = f.read()
    for num in data.split():
        print(num)
        sum += int(num)
    return sum


print(function_4("hello.txt"))
