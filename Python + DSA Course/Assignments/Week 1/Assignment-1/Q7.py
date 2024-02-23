# Question 7:Check if number entered by the user is divisible by 3 or not
num = float(input("Enter a number: "))
reminder = num % 3
if reminder == 0:
    print("Number is divisible by 3.")
else:
    print("Number is not divisible by 3.")
