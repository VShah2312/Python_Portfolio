# Q4. Write a Python program to add two numbers entered by the user.
# Method 1: 
x= int(input("Enter First number: "))
y= int(input("Enter Second number: "))
print(x+y)

# Method 2: 
x,y= input("Enter two numbers seperated by space: ").split(" ")
print(int(x)+ int(y))

# Q5. Convert a string to an integer and vice versa.
x= "5"
y= 6
print(x, type(x), y, type(y))
x_converted= int(x)
y_converted = str(y)
print(x_converted, type(x_converted), y , type(y_converted))

# Q6. Write a Python program to calculate the area of a rectangle using user
# input for length and width.
x= input("Enter length of the rectangle: ")
y= input("Enter width of the rectangle: ")
area= float(x)* float(y)
print("Area of rectangle is ", int(x)* int(y) )

# Q7. Write a Python program to calculate the average of three numbers
# entered by the user.
x,y,z= input("Enter three numbers seperated by comma: ").split(",")
avgerage= (int(x)+int(y)+int(z))/ 3
print(f"Average of the numbers is {avgerage}")

# Q8. Convert a float to an integer and vice versa.
x= int(input("Enter an integer:"))
y= float(input("Enter an float:"))
print(x, type(x), y, type(y))
x_converted= float(x)
y_converted = int(y)
print(x_converted, type(x_converted), y_converted , type(y_converted))


# Q9. Write a program that converts a temperature in Fahrenheit to Celsius.
# The formula is: Celsius = (Fahrenheit - 32) * 5/9.
f= input("Enter temperature in Farenheit: ")
c= (float(f) -32) * 5/9
print(f"{f} Fahrenheit = {c} Celsius")

# Q10. Calculate sum of 5 subjects and Find percentage.
s1,s2,s3,s4,s5= input("Enter 5 subjects marks out of 100 seperated by comma: ").split(",")
percent= (float(s1)+ float(s2)+float(s3)+float(s4)+ float(s5))/ 500 * 100
print(f"Overall percentage: {percent}%")

# Q11. Ask number of games played in a tournament. Ask the user number of
# games won and number of games loss. Calculate number of tie and total
# Points. (1 win= 4 points, 1 tie =2 points)
total= int(input("Enter number of games played: "))
wins= int(input("Enter number of games won: "))
loss = int(input("Enter number of games lost: "))
tie = total-wins-loss
total_points= (wins* 4)+ (tie* 2)
print(f"{tie} games ended in tie with total points of {total_points}")