"""
Question 2: Write a function to remove duplicates from a list and print them.
"""


def removeDuplicates(a: list[int]) -> list:
    duplicate = []
    for i in a:
        if a.count(i) > 1:
            duplicate.append(i)
    return duplicate


a: list[int] = [34, 2323, 3434, 22, 22, 34]

print(removeDuplicates(a))
