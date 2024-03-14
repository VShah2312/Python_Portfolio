"""
Question 3: Write a python program to check if the list contains three consecutive
common numbers in Python.
"""

a = [1, 1, 1, 64, 64, 64, 22, 22, 22]
result = []


def cosecutiveCommon(a: list[int]) -> list | str:
    for i in range(len(a) - 2):
        if a[i] == a[i + 1] == a[i + 2]:
            if a[i] not in result:
                result.append(a[i])
    return result


print(cosecutiveCommon(a))
