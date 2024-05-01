# Find Sum of first N natural number using backtrack recurssion:


def func(i, n, sum=0):
    print(sum)
    if i < 1:
        return
    func(i - 1, n, sum + i)


func(5, 5)
