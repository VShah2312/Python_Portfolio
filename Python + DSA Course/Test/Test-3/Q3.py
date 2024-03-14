"""
Question 3: Write a function named armstrongRange which accepts 2 integers n1
and n2. Print all the numbers from n1 to n2 which are armstrong numbers.
Example
Enter the starting number: 56
Enter the ending number: 1000
Armstrong numbers between 56 and 1000 are:
153
370
371
407
"""


def sumOfDigits(n: int) -> int:
    sum = 0
    num = n
    length = len(str(n))

    while True:
        last_digit = num % 10
        num = num // 10
        sum = sum + (last_digit**length)
        if num == 0:
            break
    return sum


def armstrongRange(n1: int, n2: int) -> None:
    for i in range(n1, n2 + 1):
        if sumOfDigits(i) == i:
            print(i)


armstrongRange(56, 1000)


def is_armstrong(num: int) -> bool:
    result = 0
    temp = num
    while temp > 0:
        last_digit = temp % 10
        result = result + (last_digit**3)
        temp //= 10

    return result == num


def armstrongRange(n1: int, n2: int) -> None:
    for num in range(n1, n2 + 1):
        if is_armstrong(num):
            print(num)


armstrongRange(56, 1000)
