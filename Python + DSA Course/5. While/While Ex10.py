# Example 10: Factors of a number, count factors and check if it is a prime number or not.


def factor(num: int = 0) -> int:
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            count += 1
        i += 1
    return count


def checkPrime(n: int) -> bool:
    if factor(n) != 2:
        return False
    return True


print(checkPrime(10))

print(123 % 100000)
