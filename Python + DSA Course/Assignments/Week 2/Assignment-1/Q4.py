# Question 4: Attempt Week 1 - Assignment 2 (Q6) and Week 1 - Assignment 2 (Q7)using function.
"""
Question 6:Ask 4 numbers from user. Make sure all the numbers entered by user are different. Print which number is the smallest.

Question 7:Take Salary as input from User and Update the salary of an employee.
  salary less than 10,000, 5 % increment
  salary between 10,000 and 20, 000, 10 % increment
  salary between 20,000 and 50,000, 15 % increment
  salary more than 50,000, 20 % increment

"""


def smallest(num1: int = 0, num2: int = 0, num3: int = 0, num4: int = 0):
    smallest = num1
    if num2 < smallest:
        smallest = num2
    if num3 < smallest:
        smallest = num3
    if num4 < smallest:
        smallest = num4

    print(smallest)


smallest(2, 5, -6, 8)


def salaryIncrement(salary: float = 0):

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

    print(f"New salary = {new_salary:.2f}")


salaryIncrement(25000)
