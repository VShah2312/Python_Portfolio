# Print Hello world n times:
# Parametrize:


def func(n) -> None:
    if n <= 0:
        return
    print("Hello World")
    func(n - 1)


func(3)
