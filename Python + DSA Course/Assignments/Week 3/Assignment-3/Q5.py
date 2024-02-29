"""
Question 5:  Create a function countOddEven that accepts an List of Integers and
print how many even and odd numbers are there.
"""


def countOddEven(my_list: list[int]) -> int | str:
    total_even = 0
    total_odd = 0
    for i in my_list:
        if i % 2 == 0:
            total_even += 1
        else:
            total_odd += 1
    return f"Total Even numbers = {total_even} \n Total Odd numbers = {total_odd}"


a = [3, 60, 9, 120, 18, 24, 15]

print(countOddEven(a))
