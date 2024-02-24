# 1, 11, 111, 1111,...


def pattern(n: int):
    i = 1
    num = 0
    while i <= n:
        num += 1
        print(num, end=" ")
        num *= 10
        i += 1


pattern(2)
pattern(4)
