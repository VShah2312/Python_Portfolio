# 10 20 30 40 50 60


def pattern(n: int):
    i = 1
    while i <= n:
        print(i * 10, end=" ")
        i += 1


pattern(10)

# Method: 2
# i is only for running the loop n times. r+


def pattern(n: int):
    i = 1
    num = 0
    while i <= n:
        num += 10
        print(num, end=" ")
        i += 1


pattern(10)
