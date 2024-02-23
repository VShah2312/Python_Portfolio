# Question 3: Write a program to check if number is divisible by 2 and 3 but not by 8

num: int = int(input("Enter a number: "))

if num % 2 == 0 and num % 3 == 0 and num % 8 != 0:
    print(f"Number {num} is divisible by 2 and 3 but not by 8")
else:
    print("Try again!")
