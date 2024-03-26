"""
Question 3: Given a string S, containing numeric words, the task is to convert the
given string to the actual number.
Input: S = “zero four zero one”
Output: 0401
Input: S = “four zero one four”
Output: 4014
"""


def wordsNum(string: str):
    dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
    }
    return dict[string]


def function(my_string: str) -> str:
    string = my_string.split()
    result = [str(wordsNum(i)) for i in string]
    return "".join(result)


s = "four zero one four"
print(function(s))
s = "zero four zero one"
print(function(s))
