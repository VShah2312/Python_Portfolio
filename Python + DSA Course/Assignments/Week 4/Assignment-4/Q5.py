"""
Question 5:  Write a function which accepts a String as a parameter and return each
word being in reverse.
"""


def reversedWords(my_string: str) -> str:
    result = my_string.split()
    result_2 = [i[::-1] for i in result]
    return " ".join(result_2)


user_input = input("Enter string: ")
print(reversedWords(user_input))
