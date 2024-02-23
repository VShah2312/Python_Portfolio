# Question 1: Write a program that takes two numbers as input and checks if the first number is divisible by the second.

num1: int = int(input("Enter num1: "))
num2: int = int(input("Enter num2: "))

if num1 % num2 == 0:
    print(f"{num1} is divisible {num2}.")
else:
    print(f"{num1} is not divisible {num2}.")
