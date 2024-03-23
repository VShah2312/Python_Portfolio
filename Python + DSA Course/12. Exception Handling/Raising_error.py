"""
Raising an error: 
Assert is one way 
"""

try:
    age = int(input("Enter age: "))
    if age < 18:
        # raise ZeroDivisionError("Age cannot be less than 18") # Here we are deciding which error to raise and what message to see.
        raise Exception(
            "Age cannot be less than 18"
        )  # Here we are raising exception with specific error message.
    print("You can vote!")
except Exception as e:
    print(type(e).__name__)
    print(e)
