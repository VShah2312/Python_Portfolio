"""
Question 7: Write different ways to remove i’th character from string in Python. Ask
i from user.
"""


# Removes first occurence
def function1(my_string: str) -> str:
    char = input("Enter index of character you want to remove: ")
    my_list = list(my_string)
    my_list.remove(char)
    return "".join(my_list)


# Removes all occurences
def function2(my_string: str) -> str:
    char = input("Enter index of character you want to remove: ")
    result = [i for i in my_string if i != char]
    return "".join(result)


print(function1("abcdaa"))
print(function2("abcdaa"))
