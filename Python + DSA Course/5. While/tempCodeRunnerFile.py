num:int= int(input("Enter a number: "))

i: int = num*-1
j:int= num
if i <0: 
    while i<=num:
        print(i, end=" ")
        i += 1
    print()
else: 
    while j<=i:
        print(j, end=" ")
        j += 1
    print()