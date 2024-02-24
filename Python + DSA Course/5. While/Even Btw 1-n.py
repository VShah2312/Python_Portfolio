# Example: 6 From 1 to 100, how many even numbers are there?
start: int = int(input("Enter start: "))
end: int = int(input("Enter end: "))

i: int = start
count = 0
while i <= end:
    if i % 2 == 0:
        count += 1
    i += 1
print(count)
