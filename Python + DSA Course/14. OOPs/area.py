"""
Make a class named area

There are no attributes related to area.
But should have 4 methods, rectangle, square, circle, triangle. 
rectangle
l,b ->input
square
s-> input
circle
r-> parameter
triangle
b,h -> parameter
"""

import math


class Area:
    def rectangle(self) -> str:
        length = float(input("Enter a length: "))
        breadth = float(input("Enter a breadth: "))
        return f"Area of rectangle is {length * breadth}"

    def square(self) -> str:
        side = float(input("Enter a side: "))
        return f"Area of square is {side**2}"

    def circle(self, radius=0) -> str:
        area = 2 * math.pi * radius
        return f"Area of circle is {area}"

    def triangle(self, breadth=0, height=0) -> str:
        area = 0.5 * breadth * height
        return f"Area of triangle is {area}"


object = Area()
print(object.circle(8))
print(object.rectangle())
print(object.square())
print(object.triangle(5, 6))
