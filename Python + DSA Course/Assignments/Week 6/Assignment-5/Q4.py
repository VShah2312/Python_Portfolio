"""
Question 4: Convert Snake case to Pascal case.
Input: python_is_great
Output: PythonIsGreat
Input: we_are_learning_python_programming
Output: WeAreLearningPythonProgramming
"""


def snakeToPascal(my_string: str) -> str:
    string = my_string.title().split("_")
    return "".join(string)


my_string = "python_is_great"
print(snakeToPascal(my_string))
my_string = "we_are_learning_python_programming"
print(snakeToPascal(my_string))

# Solution:
test_str = "we_are_learning_python_programming"
res = test_str.replace("_", " ").title().replace(" ", "")
print(res)
