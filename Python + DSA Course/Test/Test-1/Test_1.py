# Test 1
# Question 1: Write a program to print absolute value of a number entered by user.

num: int = int(input("Enter a number: "))

if num >= 0:
    print(f"Absolute Value of {num} is {num}")
else:
    abs = num * -1
    print(f"Absolute Value of {num} is {num}")

# Question 2: Given three angles of a triangle, determine whether it is an acute, obtuse, or right_angled triangle.

angle1, angle2, angle3 = input(
    "Enter three angles of a triangle seperated by comma: "
).split(",")

angle1: float = float(angle1)
angle2: float = float(angle2)
angle3: float = float(angle3)

if angle1 + angle2 + angle3 == 180:  # Sum of 3 angles of triangles has to be 180.
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("Its a right angled triangle.")
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        print("Its a obtuse angled triangle.")
    else:
        print("Its a acute angled triangle. ")
else:
    print("Triangle not possible.")

# Question 3: What will be the output of following expression, try to guess without running.
# 1+(3-4)*2**10//6 -> -170

print(1 + (3 - 4) * 2**10 // 6)

# Question 4: What will be the output of the following Python Code snippet?
# print(type(5/2)) -> float
# print(type(5//2)) -> int

print(type(5 / 2))
print(type(5 // 2))

# Question 5: What will be the out of the following code?
# print(2**4 + (5+5)**(1+1)) -> 116
print(2**4 + (5 + 5) ** (1 + 1))

# Question 6: Guess the output
"""
a=True 
b= False 
c=True 
result= (a and b )or (not c)
print(result)

result= (T and F) or (not T)
result = (F) or (F) -> F
"""

a = True
b = False
c = True
result = (a and b) or (not c)
print(result)

# Question 7: Guess the output
"""
a=10
b=20
c=5
result= (a>b)or(not(c>b))and (a+b==30)
print(result)

result= (F) or (not(F)) and (T)
result= F or T and T
result= F or T -> T 
"""
a = 10
b = 20
c = 5
result = (a > b) or (not (c > b)) and (a + b == 30)
print(result)

# Question 8: Guess the output
"""
m=7
n=3
result= (m//n==2) and (m%n==1)or(m+n>10)
print(result)

result = T and T or F
result = T or F -> T
"""
m = 7
n = 3
result = (m // n == 2) and (m % n == 1) or (m + n > 10)
print(result)

# Question 9: Guess the output
"""
value=15
result= (value<10) or (value %2==0) and (value//5==3)
print(result)

result= F or F and T
result = F or F -> F
"""

value = 15
result = (value < 10) or (value % 2 == 0) and (value // 5 == 3)
print(result)
