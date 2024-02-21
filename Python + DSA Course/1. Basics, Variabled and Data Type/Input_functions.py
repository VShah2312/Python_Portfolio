# Input: Get a data from user. By default data is save in string format.

name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Your name is {name}")
print(f"Your age is {age}", type(age))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print(n1 + n2)

n1, n2, n3, n4, n5 = input("Enter five values seperated by ,: ").split(",")
print(n1, n2, n3, n4, n5)

# Example:
name = input("Enter your name: ")  # is in string data type.
age = int(input("Enter your age: "))  # will be in int data type.
gender = input("Enter your gender: ")  # is in string data type.
print(f"My name is {name}. My age is {age}. My gender is {gender}")
