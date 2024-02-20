# Different ways of printing variables

name = "Vrunda"
age = 27
gender = "Female"

# Method:
print(name, age, gender)  # Prints all variables in one lines seperated by spaces.

print("My name is ", name)
print("My age is ", age)
print("My gender is ", gender)
# OR
print("My name is ", name, "My age is ", age, "and my gender is ", gender)

# Method  (F-string)
print("My name is {name}")  # Thus f is very important.
print(f"My name is {name}. My age is {age}. My gender is {gender}.")

# Way to debug
# Print name= Vrunda, age=27, gender =Female
print(
    f"name ={name}"
)  # We can check what values is currently assigned to a particular variable name. Doesnt show data type

print(
    f"{name = }"
)  # (this gives name result as above) name= 'Vrunda', also shows name is in string data type.
print(f"age= {age}")
print(f"{name =},{age = }")
