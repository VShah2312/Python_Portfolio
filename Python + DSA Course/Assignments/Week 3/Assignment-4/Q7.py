"""
Question 7: Make two lists of same length and pass it to a function. Return a third
list where each element is the sum of index
"""


def addition(list_1: list[int], list_2: list[int]) -> list[int]:
    if len(list_1) != len(list_2):
        return "Enter two list of same lengths."
    else:
        result = []
        for i in range(len(list_1)):
            result.append(list_1[i] + list_2[i])
        return result


my_list1 = [43, 11, 92, 22]
my_list2 = [-100, -200, 221, 100]

x = addition(my_list1, my_list2)
print(x)
