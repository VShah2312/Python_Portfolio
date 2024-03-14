"""
Question 5: Write a program to put all the common elements (in 2 lists) in another
list and print it using function.
"""


def common(lst_1: list[int], lst_2: list[int]) -> bool:
    common = []
    for val in lst_1:
        if val in lst_2:
            common.append(val)
    return common


my_list1 = ["Anirudh", "xyz", 98, 11.908, 93, -100]
my_list2 = [9008, 9102, 4311, 222, 98]

print(common(my_list1, my_list2))
