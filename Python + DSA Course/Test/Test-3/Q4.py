"""
Question 4: Write a Python program to check if a triangle is equilateral, isosceles or
scalene.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.
"""


def checkTriangle(s1: int | float, s2: int | float, s3: int | float) -> str:
    while s1 + s2 > s3 or s1 + s3 > s2 or s2 + s3 > s1:
        if s1 == s2 == s3:
            return "Equilateral"
        elif s1 == s2 or s2 == s3 or s1 == s3:
            return "Isosceles"
        else:
            return "Scalene"
    return "Enter valid values for side of triangle. "


print(checkTriangle(5, 5, 23))


def checkTriangle(a: float, b: float, c: float):
    if a == b == c:
        return "Equilateral"
    elif a == b or a == c or b == c:
        return "Isosceles"
    else:
        return "Scalene"


a = float(input("Enter the length of side a = "))
b = float(input("Enter the length of side b = "))
c = float(input("Enter the length of side c = "))

if a + b > c and a + c > b and b + c > a:
    triangle = checkTriangle(a, b, c)
    print(f"Type of triangle is = {triangle}")
else:
    print("The given side lengths cannot form a triangle.")
