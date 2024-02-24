
def middle(n1: int = 0, n2: int = 0, n3: int = 0):
    print(n1, n2, type(n3))

    if n1 <= n2 <= n3:
        mid = n2
    elif n2 <= n1 <= n3:
        mid = n1
    elif n1 <= n3 <= n2:
        mid = n3
    return mid


print(middle(1, 8))
if 8 <= 1 <= 5:
    print(True)
else:
    print(False)
