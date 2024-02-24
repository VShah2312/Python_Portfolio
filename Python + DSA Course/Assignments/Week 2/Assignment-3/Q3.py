"""
Question 3: Create a function named multiplicationTable that takes an integer
num as an argument. Print the multiplication table of that number up to 10
numbers.
"""


def multiplicationTable(n: int) -> None:
    i = 1
    while i <= 10:
        print(f"{n} x {i} = {n*i}")
        i += 1


n: int = int(input("Enter a number: "))
multiplicationTable(n)
