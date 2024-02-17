# Conditional Statements 
# if-else
# Ask for age to user
# indentation is very important
age= int(input("Enter your age: "))
if age>=18: 
    print("You can vote!")
else: # Not condition entered 
    print("You can't vote!")

# Practice Problem: 
# Ask user for 2 numbers and print which number is greater

num1, num2= input("Enter two numbers seperated by , ").split(",")
num1=float(num1)
num2= float(num2)

if num1>num2: 
    print("Number one is greater")
else:
    print("Number two is greater")

# Practice Problem: 
# Ask user for a number and print if number is odd or even

num= float(input("Enter a number: "))

if num %2==0: # Checking if number is even
    print("Number is even.")
else:  # Else number is odd
    print("Number is odd.")

# Practice Problem: 
# Ask user to enter physics and chemistry grades and print PASS, if student has passed in both else fail

phys= float(input("Enter your Physics grade: "))
chem= float(input("Enter your Chemistry grade: "))

if phys>=70 and chem>=70:
    print("PASS")
else: 
    print("FAIL")