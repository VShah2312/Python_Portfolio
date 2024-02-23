# Example: 5 Ask start, end and sum them.
start: int = int(input("Enter start: "))
end: int = int(input("Enter end: "))

i: int = start
total: int = 0
while i <= end:
    total += i
    i += 1
print(f"Sum of numbers from {start} and {end} is {total}")
