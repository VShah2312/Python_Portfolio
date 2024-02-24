"""
Question 4: Create a function named calSum which takes an 2 integer (n1 and n2)
as an argument. Calculate the sum of all the numbers divisible by 5
between n1 and n2 and return that sum. (Make sure that n1 is less than n2).
"""


def calSum(n1: int, n2: int) -> int | str:
    if n1 <= n2:
        i: int = n1
        sum: int = 0
        while i <= n2:
            if i % 5 == 0:
                sum += i
            i += 1
        return sum
    return "Make sure that n1 is less than n2"


n1: int = int(input("Enter n1: "))
n2: int = int(input("Enter n2: "))
print(calSum(n1, n2))
