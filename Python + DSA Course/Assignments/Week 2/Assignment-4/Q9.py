"""
Question 9: Ask a number from user. Print if that number is prime or not, use
functions.
"""

# With While Loop:


def factors_w(n: int) -> int:
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count


# def checkPrime_w(n: int) -> bool:
#     factors_w(n) == 2:
#         return True
#     return False


# Above can be rewritten as:
def checkPrime_w(n: int) -> bool:
    return factors_w(n) == 2


# n: int = int(input("Enter a number: "))
# if checkPrime_w(n): #True
#     print("Number is prime")
# else:
#     print("Number is not prime")


# With For Loop:
def factors_f(n: int) -> int:
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
        i += 1
    return count


# def checkPrime_f(n: int) -> bool:
#     if factors_f(n) == 2:
#         return True
#     return False


def checkPrime_f(n: int) -> bool:
    return factors_w(n) == 2


# n: int = int(input("Enter a number: "))
# if checkPrime_f(n):
#     print("Number is prime")
# else:
#     print("Number is not prime")
