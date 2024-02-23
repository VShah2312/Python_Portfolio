# Example 4: Ask M and N from user.
m: int = int(input("Enter M: "))
n: int = int(input("Enter N: "))

i: int = m
j: int = n
if m <= n:
    while i <= n:
        print(i, end=" ")
        i += 1
else:
    while j <= m:
        print(j, end=" ")
        j += 1
print()

# Add number 1 to 10
i: int = 1
total: int = 0
while i <= 10:
    total += i
    i += 1

print(total)
