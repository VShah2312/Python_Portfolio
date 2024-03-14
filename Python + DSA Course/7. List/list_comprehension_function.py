def div(num: int) -> bool:
    return num % 5 == 0 and num % 4 == 0


# Ternary is when to add here.
my_list = [i for i in range(1, 101) if div(i)]
print(my_list)


def factors(n: int) -> int | str:
    if n <= 0:
        return "Enter a valid number."
    i: int = 1
    count: int = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count


def checkPrime(n: int) -> bool | str:
    if n <= 0:
        return "Enter a valid number."
    return factors(n) == 2


# Returns all the prime numbers between 1 and 101 When to add
my_list = [i for i in range(1, 10) if checkPrime(i)]
print(my_list)
# What to add ternary:
my_list = [f"{i} -Prime" if checkPrime(i) else f"{i} -Composite" for i in range(1, 10)]
print(my_list)
