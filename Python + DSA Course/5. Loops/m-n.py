# Example 3: Ask M and N from user. Print M to N

m: int = int(input("Enter M: "))
n: int = int(input("Enter N: "))
i: int = m
while i <= n:
    print(i, end=" ")
    i += 1
print()

# Example: Ask M and N or N to M  from user.
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

# Method 2:


def nTom(m: int, n: int) -> int:
    i = m
    while i <= n:
        print(i, end=" ")
        i += 1


m: int = int(input("Enter M: "))
n: int = int(input("Enter N: "))

if m < n:
    nTom(m, n)
else:
    nTom(n, m)
