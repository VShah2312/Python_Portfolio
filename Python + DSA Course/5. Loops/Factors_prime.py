# Example 10: Factors of a number, count factors and check if it is a prime number or not.


def numberofFactor(num: int = 0) -> int:
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            # print(i, end=" ")  # Gives all the factors.
            count += 1  # Gives number of factors of a number.
        i += 1
    return count


# def checkPrime(n: int) -> bool:
#     if numberofFactor(n) != 2: #Number is prime if it has only two factors. # Observe we are calling function from above.
#         return False
#     return True


def checkPrime(n: int) -> bool:
    return numberofFactor(n) == 2  # If number of factor is 2, then it returns True.


n: int = int(input("Enter a number: "))

if checkPrime(n):  # As checkPrime function returns bool.
    print("It is a prime number.")
else:
    print("It is not a prime number.")
