"""
Question 2: Create a function named calSum() which takes 2 integers n1 and n2 as
a argument. Calculate the sum of all the numbers from n1 and n2 and
RETURN THAT SUM. Also make sure that n1 is smaller than n2. If it is not,
then return “n1 should be smaller”.
"""


def calSum(n1: int, n2: int) -> int | str:
    if n1 < n2:
        i: int = n1
        sum: int = 0
        while i <= n2:
            sum += i
            i += 1
        return sum
    return "n1 should be smaller"


n1: int = int(input("Enter n1: "))
n2: int = int(input("Enter n2: "))

print(calSum(n1, n2))
