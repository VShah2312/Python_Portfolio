# Find Sum of first N natural number:

# Method 1: Parametrize


def func(i, sum):
    if i < 1:
        print(sum)
        return
    func(i - 1, sum + i)


func(5, 0)
