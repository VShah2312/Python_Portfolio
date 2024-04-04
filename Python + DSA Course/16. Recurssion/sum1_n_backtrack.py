# Find Sum of first N natural number using backtrack recurssion:


def func(i, n, sum):
    if i > n:
        print(sum)
        return
    func(i + 1, n, sum + i)


func(1, 5, 0)
