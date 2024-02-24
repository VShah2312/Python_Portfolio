# 1 3 6 8 11 13 16 18 21 23....


def pattern(n: int):
    i = 1
    num = 1
    print(num, end=" ")

    while i < n:
        if i % 2 == 0:
            num += 3
            print(num, end=" ")
        else:
            num += 2
            print(num, end=" ")
        i += 1


pattern(4)
