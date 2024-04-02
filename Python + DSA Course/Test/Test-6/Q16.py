"""
Question 16:  Write a python program for a given long integer, we need to find if the
difference between sum of odd digits and sum of even digits is 0 or not.
The indexes start from zero (0 index is for the leftmost digit).
"""


def function(num: int) -> str:
    odd_sum = 0
    even_sum = 0
    my_string = str(num)
    for i in range(len(my_string)):
        if i % 2 == 0:
            even_sum += int(my_string[i])
        else:
            odd_sum += int(my_string[i])
    if odd_sum - even_sum == 0:
        return "Yes"
    return "No"


print(function(1212112))
print(function(12345))
