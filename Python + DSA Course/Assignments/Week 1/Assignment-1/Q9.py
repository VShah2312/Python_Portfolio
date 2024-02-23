# Question 9:Take values of length and breadth of a rectangle from user and check if it is a square or not
length = float(input("Enter length of a rectangle: "))
breadth = float(input("Enter breadth of a rectangle: "))
if length == breadth:
    print(f"It's a square")
else:
    print("It's not a square")
