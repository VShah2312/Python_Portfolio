"""
Question 4: Write a Python program that takes four numbers from the user.
Implement a function to find the average of the first three numbers. Then,
create another function to check if the average is greater than or equal to
the fourth number. Make sure to use these two functions to determine and
print whether the average is greater than or equal to the fourth number or
not.
"""

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
n4 = int(input("Enter the fourth number: "))


def average_3(n1: int = 0, n2: int = 0, n3: int = 0) -> float:
    average = (n1 + n2 + n3) / 3
    print(f"The average of {n1}, {n2}, and {n3} is: {average}")
    return average


def compar(a: float, n4: float) -> str:
    if a >= n4:
        return f" The average is greater than or equal to {n4}"
    return f"The average is less than {n4}."


print(compar(average_3(n1, n2, n3), n4))
