# Question 5: Calculate area of sqaure by taking side from the user
side = float(input("Enter value of side of a square: "))
area = side**2
print(f"Area of square with side {side} is {area} sq.ft")

print(
    f"Area of square with side {side} is {area:.2f} sq.ft"
)  # To display output upto 2 decimals only
