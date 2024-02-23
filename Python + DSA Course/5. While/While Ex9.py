# Example 9: Find sum of all the number from 1 to n1 whose i%n2 ==0
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
