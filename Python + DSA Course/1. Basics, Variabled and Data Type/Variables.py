# We use variables to call data that is stored in temporary memory.
# We can use "=" to assign value to a variable.

x = 5
y = 22
z = x + y
first = "Vrunda"
last = "Shah"
name = first + last
print(x)
print(y)
print(z)
print(name)

"""
Rules for naming a variable: 
1. Should always start with a-z, A-Z, _
2. Can contain a-z, A-Z, _,0-9
3. Cannot use reserved keywords (if, else, etc. total 35 of those keywords)

Questions: Can below be a variable name
1. abc -> yes
2. abc123 -> yes
3. abc_1_2_3 -> yes
4. _abc -> yes
5. first_name -> yes
6. first name -> no
7. ___abc -> yes
8. ___ -> yes
9. a&8a ->no
"""
