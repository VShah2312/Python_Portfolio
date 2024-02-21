# Escape Sequence (always comes in "" or ''), 

print("Hello World \nThis is Vrunda Shah") # \n is new line 
print ("This is \t\t\t Vrunda Shah") # \t is one tab 
print ("This is \" Vrunda Shah \" ") # \"
print ('This is \' Vrunda Shah \' ' ) # \'
print( "This is Vrunda \\ Shah ") # \\
print( "This is Vrunda\b Shah ") #\b is backspace

# Example: print your name, age and gender in three different lines using one print statements
print("My name is Vrunda Shah.\nMy age is 12. \nMy gender is female.")

# Output: My name is A\nirudh
print("My name is A\\nirudh")
print("My name is A\\\\nirudh") # For double slash
print("My name is \"Anirudh\"")
print('My name is "Anirudh"')

# You can always miss match the "", '' when you want one in string output. 
# Other method is \" \"

# Example: 
# Output: a"\/\"xyz'"\
print("a\"\\/\\\"xyz'\"\\")