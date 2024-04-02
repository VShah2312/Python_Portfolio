"""
Question 15: Python Program for Find sum of odd factors of a number.
"""


def factors(num: int) -> list:
    my_list = []
    for i in range(1, num):
        if num % i == 0:
            my_list.append(i)
    return my_list


num: int = int(input("Enter a number: "))
result = factors(num)
output = sum([i for i in result if i % 2 != 0])
print(f"Output: {output}")
