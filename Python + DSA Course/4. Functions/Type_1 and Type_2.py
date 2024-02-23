# 1. Without Parameters, without return
# 2. With Parameters, without return


# Example 1:
def greet(x, y, z):  # Greet functions has 3 parameters here namely x,y and z
    # x, y and z are local variables.
    print(f"x={x}")
    print(f"y={y}")
    print(f"z={z}")


# greet()  # Zero arguments
greet(5, 6, 3)  # 3 arguments 5,6, 3
# greet(6,7,8,9) # Throws error because we are entering more then required. 4 arguments here 6,7,8,9
greet("Yes", 6, True)


# Example 2:
def greet_1(name: str, age: int, gender: str):
    # name, age and gender are local variables.
    print(f"My name is {name}.")
    print(f"My age is {age}.")
    print(f"My gender is {gender}.")


greet_1("Vrunda", "27", "Female")
# This would work but if you hover over it will tell which data type should your each arguments be.

greet_1("Vrunda", 27, "Female")  # This is correct way.

greet_1(
    27, 27, "Female"
)  # This will also work. Wrong value for argument, wrong answer.


# Example 3:
def greet_1(name: str, age: int, gender: str):
    # name, age and gender are local variables.
    name = ""
    age = 0
    gender = ""
    print(f"My name is {name}.")
    print(f"My age is {age}.")
    print(f"My gender is {gender}.")


n = "Vrunda"
a = 27
g = "Female"
greet_1(n, a, g)
print(n, a, g)


# Example 4:
def greet_1(name: str, age: int, gender: str):
    # name, age and gender are local variables.
    print(f"My name is {name}.")
    print(f"My age is {age}.")
    print(f"My gender is {gender}.")


# name, age and gender are global variables.
name = "Vrunda"
age = 27
gender = "Female"
greet_1(name, age, gender)
print(name, age, gender)
# No change in result. Same result as example 3.
