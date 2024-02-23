# Introduction:
"""
i=1
while i<=10: 
    print("Hello World ")

Above is an infinite loop as value of i will always be 1. 
So we need to add counter or increase it by 1 after every print. 
"""

i = 1
while i <= 10:
    print("Hello World!")
    i += 1

# Same output for both.
i = 1
while i <= 10:
    i += 1
    print("Hello World!")

# Example 1: Print 1 to 10 using while loop

i: int = 0
while i < 10:
    i += 1
    print(i, end="")

# Example 2: Print 1 to n, get n from user.

n: int = int(input("Enter n: "))
i: int = 1
while i <= n:
    print(i)
    i += 1


# How to write above in a function?
def printPattern(n: int) -> None:
    i: int = 1
    while i <= n:
        i += 1
    print(i, end="")


# Example 3: Ask M and N from user. Print M to N

m: int = int(input("Enter M: "))
n: int = int(input("Enter N: "))
i: int = m
while i <= n:
    print(i, end=" ")
    i += 1
print()

# Example 4: Ask M and N from user.
m: int = int(input("Enter M: "))
n: int = int(input("Enter N: "))

i: int = m
j: int = n
if m <= n:
    while i <= n:
        print(i, end=" ")
        i += 1
else:
    while j <= m:
        print(j, end=" ")
        j += 1
print()

# Add number 1 to 10
i: int = 1
total: int = 0
while i <= 10:
    total += i
    i += 1

print(total)

# Example: 5 Ask start, end and sum them.
start: int = int(input("Enter start: "))
end: int = int(input("Enter end: "))

i: int = start
total: int = 0
while i <= end:
    total += i
    i += 1
print(f"Sum of numbers from {start} and {end} is {total}")


# Example: 6 From 1 to 100, how many even numbers are there?
start: int = int(input("Enter start: "))
end: int = int(input("Enter end: "))

i: int = start
count = 0
while i <= end:
    if i % 2 == 0:
        count += 1
    i += 1
print(count)

# Example 7: From 1 to 100 how many number are divisible 3 and 2 are there?
start: int = int(input("Enter start: "))
end: int = int(input("Enter end: "))

i: int = start
count = 0
while i <= end:
    if i % 3 == 0 and i % 2 == 0:
        count += 1
    i += 1
print(count)

# Example 8: Ask a number from user n and print numbers from -n to n
num: int = int(input("Enter a number: "))

i: int = num * -1
j: int = num

if num < 0:
    while i <= j:
        print(i, end=" ")
        i += 1
    print()
else:
    while j <= i:
        print(i, end=" ")
        i -= 1
    print()

# Question 9: Find sum of all the number from 1 to n1 whose i%n2 ==0
# example: num1=5, num2= 2


def func(n1: int = 0, n2: int = 0) -> int:
    i = 1
    total = 0

    if n1 <= 0 or n2 <= 0:
        print("Enter Valid Num1 and Num2")
    else:
        while i <= n1:
            if i % n2 == 0:
                total += i
            i += 1
    return total


print(func(10, 2))


# Question 10: Factors of a number, count factors and check if it is a prime number or not.


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
