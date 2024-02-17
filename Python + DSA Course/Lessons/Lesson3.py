# Q12. Write a Python program that takes two numbers as input and
# performs the following operations: addition, subtraction, multiplication,
# division, and modulus. Display the results.
num1,num2= input("Enter two numbers seperated by , ").split(",")
num1= float(num1)
num2= float(num2)
print("Addition of two numbers is", num1+num2)
print("Subtraction of two numbers is", num1-num2)
print("Multiplication of two numbers is", num1*num2)
print("Divison of two numbers is", num1/num2)
print("Modulo of two numbers is", num1%num2)

# Q13. Write a Python program to swap the values of two variables without
# using a temporary variable.
num1,num2= input("Enter two numbers seperated by , ").split(",")
num1= float(num1)
num2= float(num2)
# Printing before the swap
print(f"Orginal two numbers are num1= {num1} and num2= {num2}") 
num1=num1+num2 # total
num2=num1-num2 # total -num2 gives you num1
num1=num1-num2 # total -num1 gives you num2
# Printing after the swap
print(f"Swapped two numers num1= {num1} and num2= {num2}")

# Q14. Write a Python program to calculate the compound interest for a
# given principal, rate of interest, and time period. Ask everything from the
# user.
principal= float(input("Enter the principal: "))
rate= float(input("Enter rate of interest in percent: "))
rate_decimal= rate/ 100 
time= float(input("Enter time in years: "))
n= float(input("Enter the number of times interested is compounded in a year: "))
future_value= principal* (1+ (rate_decimal/ n))**(n*time)
interest= future_value-principal
print(f"Future value including interest: {future_value}")
print(f"Interest accumulated over year: {interest}")

# Q15. Write a Python program that takes the radius of a circle as input and
# calculates its area. Use the formula: Area = 3.14 * r^2.
radius = float(input("Enter radius of the circle: "))
Area= 3.14 * (radius**2)
print(f"Area of the circle: {Area}")