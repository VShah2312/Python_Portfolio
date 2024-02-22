# Assignment 1:

# Question 1:
a = 5
b = 10

print(a > 5 and b >= 10)
# Answer: False and True= False

print(a >= 5 or not b > 10)
# Answer: True and not False = True and True = True

print(not (a > 5 and b > 5))
# Answer: not (False and True)= not (False)= True

print(not (a < 10 or not b < 10))
# Answer: not(True or not False)= not(True or True)= not(True)=False

print(not (not a <= 5 or not b >= 10))
# Answer: not(not True or not True ) = not(False or False)= not(False)= True


# Question 2: Write program to convert km to miles. Ask user for km.
kilo = float(input("Enter value in km: "))
miles = kilo * 0.621371
print(f"{kilo} kilometers = {miles} miles")

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

# Question 4: Ask value in Rupees and convert into paise.
rupees = float(input("Enter value in rupees:"))
paise = rupees * 100
print(f"{rupees} Rupees = {paise} Paise")

# Question 5: Calculate area of sqaure by taking side from the user
side = float(input("Enter value of side of a square: "))
area = side**2
print(f"Area of square with side {side} is {area} sq.ft")

print(
    f"Area of square with side {side} is {area:.2f} sq.ft"
)  # To display output upto 2 decimals only

# Question 6:
games_played = int(input("Enter number of games played: "))
games_won = int(input("Enter number of games won: "))
games_lost = int(input("Enter number of games lost: "))
games_tie = games_played - games_lost - games_won
total_points = games_won * 4 + games_tie * 2
print(
    f"User played {games_played} games. Won {games_won} games, lost {games_lost} and {games_tie} games tied. Total points for the user is {total_points}"
)

# Question 7:Check if number entered by the user is divisible by 3 or not
num = float(input("Enter a number: "))
reminder = num % 3
if reminder == 0:
    print("Number is divisible by 3.")
else:
    print("Number is not divisible by 3.")

# Question 8:
num = float(input("Enter a number: "))
reminder = num % 2
if reminder == 0:
    print("Number is Even.")
else:
    print("Number is Odd.")


# Question 9:Take values of length and breadth of a rectangle from user and check if it is a square or not
length = float(input("Enter length of a rectangle: "))
breadth = float(input("Enter breadth of a rectangle: "))
if length == breadth:
    print(f"It's a square")
else:
    print("It's not a square")
