# Q23. Write a Python program that takes an integer input and prints
# whether it's positive, negative. (Consider 0 as positive)
num= int(input("Enter a number: "))
if num>=0: 
    print("Number is positive")
else: 
    print("Number is negative")

# Q24. Write a program that takes a character as input and prints whether
# it's a vowel or a consonant. (Multiple OR will be used)
char= input("Enter a character: ")

if char=='e' or char=='a' or char=='i' or char=='o' or char=='u': 
    print(f"Character {char}, is a vowel")
else: 
    print(f"Character {char}, is consonant")

# Q25. Write a program that takes two numbers as input and checks if the
# first number is divisible by the second.
num1, num2 =input("Enter two numbers seperated by , ").split(",")
num1= float(num1)
num2= float(num2)
if num1 % num2== 0: 
    print("First number is divsible by the second")
else:
    print("First number is not divisible by the second")

# Q26. A student will not be allowed to sit in exam if his/her attendance is
# less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# 1. Print percentage of class attended
# 2. Print Is student is allowed to sit in exam or not.

classes_held= int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))

attendance_percent= classes_attended/classes_held * 100
print(f"Your attendance percentage is {attendance_percent}%")
if attendance_percent>=75: 
    print("You are allowed to sit in exam")
else: 
    print("You are not allowed to sit in the exam")