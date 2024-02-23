# Question 2:  Attempt the same leap year question (Week 1 - Assignment 2 - Q8) but using function.
# Try calling function with different years as a parameter and check the output
"""Question 8:An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. 
A leap year contains a leap day.
These are the conditions used to identify leap years:
a. if the year can be evenly divided by 4, it is then a leap year
b. but if the year is evenly divided by 4 and also by 100, then it is NOT a leap year
c. but if the year is evenly divided by 4 and also by 400, then it is a leap year
Ask a year input from user. And tell if the year entered by user is leap or not."""


def leapYear(year: int):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


leapYear(2004)
