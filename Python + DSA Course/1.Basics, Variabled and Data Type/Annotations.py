# Annotations
# What is the difference between  statically typed language and dynamically types language?
# For statically typed language you need to mention data type of the variable in the beginning and then data type cannot be changed.
# Keep in mind data can be changed.
# Python is dynamically typed language, mean it is based on runtime.

# So below is possible in only dynamically typed language:
a = 5
print(a)

a = "Name"
print(a)

# So is better to restrict data type of a variable? Answer is yes. Solution to this is Annotations.
# Keep in mind it is still dynamically typed. Annotations is just for users clarity/ for developers understanding.
a: int = 5
print(a)

# We can notice that we can still change data type of the variable a.
# We can change the setting so we get red/alert if enter a different data type then pre-defined.
a = "String"
print(a)

# What if we want to allow int or float
a: int | float = 55
print(a)

a = 55.6  # We dont get red line alert.
print(a)

# Moreover for example we do below
r: int = 10 / 5
# We see red line/alert and if hower over it, we see it suggest float and reminds us that we are trying to save float in int.
d: float = 10 / 5
d: int | float = 10 / 5
# Above both will work with /.
