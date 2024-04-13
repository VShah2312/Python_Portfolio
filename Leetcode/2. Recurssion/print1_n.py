# Print 1 to N using recurssion


def func(i, n):
    if i > n:
        return
    print(i)
    func(i + 1, n)


func(1, 10)


# Print 1 to N using backtrack recurssion:
def func(i, n):
    if i < 1:
        return
    func(i - 1, n)
    print(i)


func(10, 10)
