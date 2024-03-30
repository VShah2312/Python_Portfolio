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
        # length, breadth as input.
        # Here length and breadth is only used for that method. So we are not using self.length etc.
        length = float(input("Enter a length: "))
        breadth = float(input("Enter a breadth: "))
        return length * breadth

    def square(self) -> float:
        # side is input.
        side = float(input("Enter a side: "))
        return side**2

    def circle(self, radius=0) -> float:
        # radius as parameter.
        area = 2 * math.pi * radius
        return area

    def triangle(self, breadth=0, height=0) -> float:
        # breadth, height as paramter.
        area = 0.5 * breadth * height
        return area


# We could have save object class in a module and import it to use it.
object = Area()  # Here we are creating object.
print(object.circle(8))
print(object.rectangle())
print(object.square())
print(object.triangle(5, 6))
