"""
Question 12: Remove all duplicates words from a given sentence.
"""


def removeDuplicatesWords(my_string: str) -> str:
    my_list = list(my_string.split())
    result = []
    for i in my_list:
        if i not in result:
            result.append(i)
    return " ".join(result)


my_string = "pthon is great and java is great"
print(removeDuplicatesWords(my_string))
