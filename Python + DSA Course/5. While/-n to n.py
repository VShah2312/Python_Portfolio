# Example 8: Ask a number from user n and print numbers from -n to n
num: int = int(input("Enter a number: "))

i: int = num * -1
j: int = num

if num < 0:
    while i <= j:
        print(i, end=" ")
        i += 1
    print()
else:
    while j <= i:
        print(i, end=" ")
        i -= 1
    print()