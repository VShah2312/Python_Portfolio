# How to check a data type of a variable and how to convert them.
"""
Data types are different class in which variable are classified, which indicates how a variable/data will be treated. 

Data Types in python: 
1. String (str) -> "name", "char" , "1455"
2. Integer (int) -> 5,6,.0,-9
3. Float (float) -> 5.0, -55.34
4. Complex (complex) -> 3i+5j (real + imaginary)
5. Bolean (bool) -> true, false
6. List (list) -> [34, 66, 55, 12, 990]
7. Tuple (tuple) -> (34, 66, 55, 12, 990)
8. Dictionary (dict) -> {"Vrunda": 75, "Charmi": 88} key value pair

"""


x = 55
print(x)
print(x, type(x))

y = 66.7
print(y, type(y))

name = "Vrunda"
print(name, type(name))

bol = True
print(bol, type(bol))

marks = [34, 66, 55, 12, 990]
print(marks, type(marks))

marks_1 = (34, 66, 55, 12, 990)
print(marks_1, type(marks_1))

dict_1 = {"Vrunda": 75, "Charmi": 88}
print(dict_1, type(dict_1))

x = "55"
y = "10"
print(x + y)
# Returns: 5510

x = int(x)
y = int(y)
print(x + y)
# Returns: 65

"""
Type conversion/ Type casting 
To convert  from one data type to other. 
"""
# str -> float, same with int.
a = "100.5"
print(float(a), type(float(a)))  # works.
b = "10"
print(int(b), type(int(b)))  # works.

# float -> str, same with int.
a1 = 100.5
print(str(a1), type(str(a1)))  # works.
b1 = 10
print(str(b1), type(str(b1)))  # works.

# int -> float
a = 10
print(float(a))  # works

# float -> int
b = 100.5
print(int(b))  # converts to integer closer to zero (using floor function)

c = -5.55
print(int(c))  # converts to integer closer to zero (using ceiling function)

a = "100. 5"
print(float(a))  # throws an error. Value Error due to space before 5

a = " 100.05 "
print(
    float(a)
)  # doesnt throw error even though we have space at the beginning and end, as it strips the spaces. It cant strip spaces in between.

"""
int -> bol
True -> 1, 3, 600, -3, -4 etc. 
False -> 0

float -> bol
True -> 1.56, 3.3423, 600.0, -3.3424, -4.05 etc. 
False -> 0.0

str -> bol
True -> "adsada", ".", " "(space)
False -> ""
"""

a = 1
print(bool(a))
b = 0
print(bool(b))

a = -5.34
print(bool(a))
b = 0.0
print(bool(b))

a = " "
print(bool(a))
b = ""
print(bool(b))

# Short cut alt+shift+ up copies line above the line where cursor is.
# Short cut alt+shift+ down copies line below the line where cursor is.
# Short cut alt+ down moves line below the line where cursor is.
# Short cut alt+ up moves line above the line where cursor is.
# Short cut alt+shift + side arrows selects values on either side.
