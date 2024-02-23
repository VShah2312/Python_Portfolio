# Question 3: Ash 3 numbers from user and calculate the average
num1, num2, num3 = input("Enter 3 numbers seperated by comma: ").split(",")
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)
average = (num1 + num2 + num3) / 3
print(f"Average of 3 numbers is {average}")

print(
    f"Average of 3 numbers is {average:.2f}"
)  # To display output upto 2 decimals only
