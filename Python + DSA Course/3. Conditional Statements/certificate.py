"""
Requirements: 
1. Should be part of code and debug
2. Minimum class attended should be 20
3. Minimum assignment submitted==45
"""
req= input("Are you part of Code and Debug: ").lower()

if req=="yes":
    class_attended = int(input("Enter number of class attended:"))
    if class_attended >=20:
        assign_submitted =int(input("Enter number of assignment submitted: "))
        if assign_submitted >=45:
            print("You can get certificate.")
        else: 
            print("You cannot get certificate.")
    else:
        print("You cannot get certificate.") 
else: 
    print("You cannot get certificate.")    

