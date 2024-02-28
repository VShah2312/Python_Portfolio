"""
Question 6: Create a function sumCountOddEven that accepts an List of Integers
and calculate sum of even and odd numbers.

"""


def countOddEven(my_list) -> int:
    even_sum = 0
    odd_sum = 0
    for i in my_list:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return f"Sum Even numbers = {even_sum} \n Sum Odd numbers = {odd_sum}"


a = [3, 60, 9, 120, 18, 24, 15]

print(countOddEven(a))
