"""
Question 5: Write a Python program to capitalize the first and last letters of each
word in a given string.
Input: c
Output: PythoN ExerciseS PracticE SolutioN
Input: delhi is best city with 0 AQI
Output: DelhI IS BesT CitY WitH 0 AqI
"""


def function(my_string: str) -> str:
    list = my_string.split()
    result = ""
    for word in list:
        if len(word) == 1:
            result += word.upper()
            result += " "
        else:
            result += word[0].upper()
            result += word[1:-1].lower()
            result += word[-1].upper()
            result += " "
    return result


my_string = "python is a great language"
print(function(my_string))
my_string = "delhi is best city with 0 AQI"
print(function(my_string))


# Solution:
def capitalize_first_last_letters(str1):
    str1 = result = str1.title()
    result = ""
    for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]


print(capitalize_first_last_letters("python is a great language"))
print(capitalize_first_last_letters("delhi is best city with 0 AQI"))
