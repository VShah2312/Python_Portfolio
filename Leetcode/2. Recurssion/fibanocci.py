def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fib(n - 1) + fib(n - 2)


print(fib(7))
print(fib(9))

# Return list of elements:
from typing import List


def generateFibonacciNumbers(n: int, result=[0, 1]) -> List[int]:
    # Write your code here
    if n == 1 or n == 2:
        return result[:n]
    for i in range(2, n):
        result.append(result[i - 2] + result[i - 1])
    return result
