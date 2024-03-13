# Named arguments
def totalMarks(phy: int, chem: int, maths: int, eng: int, comp: int):
    total = phy + chem + maths + eng + comp
    print(f"English = {eng}")
    print(f"Physics = {phy}")
    print(f"Total marks = {total} ")


# In above functions marks will need to be ordered in provided order.
# What if we could enter marks in any order. We can do that by enter name of variable while passing the arguments.
# NO change in the function defination.

totalMarks(eng=58, phy=95, maths=85, comp=45, chem=75)

# What if we know phy and chem and enter other by name.
# Keep in mind the arguments without name needs to be on the right.
totalMarks(58, phy=95, maths=85, comp=45, chem=75)
# This will throw error as value without name is for phy position and we defined phy again too
# So variable value without name needs to be exact position as the variable.


# We could also have default value if not mentioned.
def totalMarks(
    phy: int = 0, chem: int = 0, maths: int = 0, eng: int = 0, comp: int = 0
):
    total = phy + chem + maths + eng + comp
    print(f"English = {eng}")
    print(f"Physics = {phy}")
    print(f"Total marks = {total} ")


totalMarks()  # No arguments entered it will take default value


# For example if we want phy, chem and math to be required arguments and other to be optional.
# We can do that. Keep in mind all required goes first, then optional.
# Hower over function will show all the details.
def totalMarks(phy: int, chem: int, maths: int, eng: int = 0, comp: int = 0):
    total = phy + chem + maths + eng + comp
    print(f"English = {eng}")
    print(f"Physics = {phy}")
    print(f"Total marks = {total} ")


# totalMarks()  # Will throw error as it requires 3 arguments at min.
totalMarks(98, 25, 25)
