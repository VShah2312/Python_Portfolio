# Ternary If Else

age = 20
if age >= 18:
    print("adult")
else:
    print("Child")
# Else is mandatory
print("Adult") if age >= 18 else print("Child")

my_list = [i % 2 == 0 for i in range(1, 11)]
print(my_list)
# What value to add? "Even" is string value we are adding
# if else is written before for loop. 
my_list = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 11)]
print(my_list)
my_list = [f"{i}-Even" if i % 2 == 0 else f"{i}- Odd" for i in range(1, 11)]
print(my_list)

# When to add? Else part will never come in this. 
# if else is written after for loop.
my_list = [i for i in range(1, 11) if i % 2 == 0]
print(my_list)
