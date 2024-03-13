# 1, 11, 111, 1111,...


def pattern(n: int):
    i = 1
    num = 0
    while i <= n:
        num += 1
        print(num, end=" ")
        num *= 10
        i += 1
    print()


pattern(2)
pattern(4)

# Method 2:


def pattern_2(n: int):
    i = 1
    num = 1
    while i <= n:
        print(num, end=" ")
        num = num + (10**i)
        i += 1
    print()


pattern_2(2)
pattern_2(4)
