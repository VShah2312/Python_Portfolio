# Assignment 2:

# Question 1: Write a program that takes two numbers as input and checks if the first number is divisible by the second.

num1: int = int(input("Enter num1: "))
num2: int = int(input("Enter num2: "))

if num1 % num2 == 0:
    print(f"{num1} is divisible {num2}.")
else:
    print(f"{num1} is not divisible {num2}.")

# Question 2: A student will not be allowed to sit in exam if his/her attendance is less then 75%. Take two inputs from user
# a. number of classes held.
# b. number of classes attended.
# Print percentage of class attended and print is student allowed to sit in exam or not.

class_held: int = int(input("Enter number of classes held: "))
class_attnd: int = int(input("Enter number of classes attended: "))

attnd_percent = (class_attnd / class_held) * 100
print(f"Percentage of class attended is {attnd_percent} %")

if attnd_percent >= 75:
    print("You are allowed to sit in the exam.")
else:
    print("You are not allowed to sit in the exam.")


# Question 3: Write a program to check if number is divisible by 2 and 3 but not by 8

num: int = int(input("Enter a number: "))

if num % 2 == 0 and num % 3 == 0 and num % 8 != 0:
    print(f"Number {num} is divisible by 2 and 3 but not by 8")
else:
    print("Try again!")

# Question 4:Ask grade from a user. 91-100-> A, 81-90-> B, 71-80 -> C, 61-70->D 0-60 ->Fail

grade: int = int(input("Enter your marks: "))

if 91 <= grade <= 100:
    print("A")
elif 81 <= grade <= 90:
    print("B")
elif 71 <= grade <= 80:
    print("C")
elif 61 <= grade <= 70:
    print("D")
elif 0 <= grade <= 60:
    print("Fail")
else:
    print("Invalid marks, please enter marks between 0 and 100")

# Question 5: Write a program to calculate bill. Ask the final amount from the user. You have to give discount and print the final bill after discount.
# 50000 above - 30% discount
# 40000 - 49999 - 25% discount
# 30000 - 39999 - 20% discount
# 10000 - 29999 - 10% discount
# 1 - 9999 - No discount
# Print the discount and the final amount to be paid.

bill_amount: float = float(input("Enter the bill amount: "))

if bill_amount >= 50000:
    discount_percentage = 30
elif 40000 <= bill_amount < 50000:
    discount_percentage = 25
elif 30000 <= bill_amount < 40000:
    discount_percentage = 20
elif 10000 <= bill_amount < 30000:
    discount_percentage = 10
else:
    discount_percentage = 0

discount_amount: float = (discount_percentage / 100) * bill_amount
final_amount: float = bill_amount - discount_amount

print(f"You got {discount_percentage}% discount")
print(f"Your final bill is Rs. {final_amount:.2f}")


# Question 6:Ask 4 numbers from user. Make sure all the numbers entered by user are different. Print which number is the smallest.
num1, num2, num3, num4 = input("Enter four numbers seperated by comma: ").split(",")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
num4 = int(num4)

smallest = num1

if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3
if num4 < smallest:
    smallest = num4

print(f"The smallest number = {smallest}")

# Question 7:Take Salary as input from User and Update the salary of an employee.
#   salary less than 10,000, 5 % increment
#   salary between 10,000 and 20, 000, 10 % increment
#   salary between 20,000 and 50,000, 15 % increment
#   salary more than 50,000, 20 % increment

salary: float = float(input("Enter the salary =  "))

if salary < 10000:
    increment = 5
elif 10000 <= salary < 20000:
    increment = 10
elif 20000 <= salary < 50000:
    increment = 15
else:
    increment = 20

increment_amount = (increment / 100) * salary
new_salary = salary + increment_amount

print(f"The new salary = {new_salary:.2f}")

# Question 8:An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. A leap year contains a leap day.
# These are the conditions used to identify leap years:
# a. if the year can be evenly divided by 4, it is then a leap year
# b. but if the year is evenly divided by 4 and also by 100, then it is NOT a leap year
# c. but if the year is evenly divided by 4 and also by 400, then it is a leap year
# Ask a year input from user. And tell if the year entered by user is leap or not.
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
