# Keep in mind:

result = ""

result += "python"  # resu't = result + "python" result is overwritten ever time.
result += "is"
result += "good"
print(result)

"""
Question: Keep asking for a string from user till "q" or "Q" is entered. Print all elements. 
"""

result = []
while True:
    user_input: str = input("Enter a string: ")
    if user_input == "q" or user_input == "Q":
        print("\n".join(result))
        break
    result.append(user_input)

# OR
result = ""
while True:
    user_input: str = input("Enter a string: ")
    if user_input.lower() == "q":  # user_input will be lower and checked. Not changed.
        print(result, end="")
        break
    result += user_input
    result += "\n"
    print(result)
