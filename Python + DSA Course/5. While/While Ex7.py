# Example 7: From 1 to 100 how many number are divisible 3 and 2 are there?
start: int = int(input("Enter start: "))
end: int = int(input("Enter end: "))

i: int = start
count = 0
while i <= end:
    if i % 3 == 0 and i % 2 == 0:
        count += 1
    i += 1
print(count)
