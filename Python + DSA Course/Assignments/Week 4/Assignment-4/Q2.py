"""
Question 2: Write a function which accepts a String as a parameter and return the
list of words.
"""


def words(my_string: str):
    result = [i for i in my_string.split()]
    return result


print(words("python is great"))
