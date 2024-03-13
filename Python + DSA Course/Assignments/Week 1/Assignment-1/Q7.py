# Question 7:Check if number entered by the user is divisible by 3 or not
num = float(input("Enter a number: "))
remainder = num % 3
if remainder == 0:
    print("Number is divisible by 3.")
else:
    print("Number is not divisible by 3.")
