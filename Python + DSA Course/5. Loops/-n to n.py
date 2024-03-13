# Example 8: Ask a number from user n and print numbers from -n to n
num: int = int(input("Enter a number: "))

if num > 0:
    i: int = num * -1  # 3 -> -3
    j: int = num  # 3
else:
    i: int = num  # -3
    j: int = num * -1  # -3 -> 3


while i <= j:
    print(i, end=" ")
    i += 1
print()
