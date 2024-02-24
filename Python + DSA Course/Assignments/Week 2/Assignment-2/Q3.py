"""
Question 3: Ask 3 numbers from user. Make a function which returns the middle of
those 3 numbers. Then make a function to check if that middle number is
divisible by both 3 and 4. Make 2 functions for reusability.
"""


def middle_2(n1: int = 0, n2: int = 0, n3: int = 0) -> int:
    if n1 <= n2 <= n3 or n3 <= n2 <= n1:
        return n2
    if n2 <= n1 <= n3 or n3 <= n1 <= n2:
        return n1
    else:
        return n3


def div3and4(num: int) -> bool:
    if num % 3 == 0 and num % 4 == 0:
        return True
    return False


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

middle_number: int = middle_2(n1, n2, n3)
print(f"The middle number is: {middle_number}")

if div3and4(middle_number) == True:
    print(f"{middle_number} is divisible 3 and 4.")
else:
    print(f"{middle_number} is not divisible 3 and 4.")
