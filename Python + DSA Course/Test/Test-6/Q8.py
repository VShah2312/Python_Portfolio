"""
Question 8: Write a program to find Maximum frequency character in String.
Return/Print the character which comes the most times in that string.
"""


def frequency(my_string: str) -> dict:
    frequency = {}
    for i in my_string:
        frequency[i] = my_string.count(i)
    most_frequency = max(list(frequency.values()))
    result = {}
    for key, value in frequency.items():
        if value == most_frequency:
            result[key] = value
    return result


print(frequency("abcacdffgfgg"))
