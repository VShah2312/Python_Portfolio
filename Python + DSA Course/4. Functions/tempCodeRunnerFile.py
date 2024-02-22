def add(): 
    # Local Variables.
    num1:int= int(input("Enter num1: "))
    num2:int= int(input("Enter num2: "))
    print(num1+num2)

num1=100
num2=200
add()
print(num1) # This will throw error as num1 is local variable. 
