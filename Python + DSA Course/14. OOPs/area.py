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
    def rectangle(self) -> float:
        length = float(input("Enter a length: "))
        breadth = float(input("Enter a breadth: "))
        return length * breadth

    def square(self) -> float:
        side = float(input("Enter a side: "))
        return side**2

    def circle(self, radius=0) -> float:
        area = 2 * math.pi * radius
        return area

    def triangle(self, breadth=0, height=0) -> float:
        area = 0.5 * breadth * height
        return area


object = Area()
print(object.circle(8))
print(object.rectangle())
print(object.square())
print(object.triangle(5, 6))
