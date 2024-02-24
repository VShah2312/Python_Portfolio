# 1 11 101 1001...


def pattern(n: int):
    i = 1
    num = 1
    while i <= n:
        print(num, end=" ")
        num = 1 + (10**i)
        i += 1


pattern(4)

pattern(1)
