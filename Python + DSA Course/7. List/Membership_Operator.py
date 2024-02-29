# Membership operator (IN/NOT IN)

a = [89, 25, 14, 89]
print(a.count(89))  # Counts occurence of a number

print(a.count(100))

# Want to know if number is in a list or not, doesnt matter the how many occurence
n: int = int(input("Enter a number: "))

if a.count(n) > 0:
    print("Yes")
else:
    print("No")

a = [89, 25, 14, 89]
if n in a:
    print("Yes")
else:
    print("No")

print(a.index(89))  # Give first occuring index of a value.
