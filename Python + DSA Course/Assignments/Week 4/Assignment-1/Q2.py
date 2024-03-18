"""
Question 2: Make your own list of numbers. Ask a start and end position from User.
Make another different list which will contain number from start to end
position. Use slicing logic.
"""

my_list = [45, 31, 76, 54, 11, 32, 100]

start: int = int(input("Enter a start number: "))
end: int = int(input("Enter a end number: "))
step: int = int(input("Enter a step: "))
result = [my_list[i] for i in range(start, end + 1, step)]
print(result)

from typing import List


def listSlice(lst: List, start: int, end: int):
    print(lst[start : end + 1])


my_list = ["Anirudh", 6, 4, 110.654, True, -54]
listSlice(my_list, 2, 4)
