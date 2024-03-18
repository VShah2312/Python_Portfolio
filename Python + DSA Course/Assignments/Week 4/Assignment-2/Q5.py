"""
Question 5: Count how many numbers are divisible by 3 and 6 between 1 to 1000
by using list comprehension.
"""


def countDiv3and6(num: int) -> int:
    x = [i for i in range(1, num + 1) if i % 3 == 0 and i % 6 == 0]
    return len(x)


print(countDiv3and6(1000))
