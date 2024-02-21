# Ask a number from user.
#Print positive, negative, equal to zero: 
num: int= input("Enter a integer: ")

#Method 1: 
if num >=0: 
    if num==0:
        print("Number is equal to zero")
    else: 
        print("Number is positive")
else: 
    print("Number is negative")

# Method 2: 
if num >0: 
    print("Positive")
else:
    if num == 0:
        print("Equal to zero")
    else:
        print("Negative")

# Gives same output. 