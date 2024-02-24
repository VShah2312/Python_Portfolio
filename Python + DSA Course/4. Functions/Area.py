def cirlce(r: float) -> float:
    return 3.14 * r**2


def rectangle(l: float, b: float) -> None:
    print(l * b)


def triangle(b: float, h: float) -> float:
    return 0.5 * b * h


def square(s: float) -> float:
    return s**2


# this part will run only when this file runs. Not in the file we are importing this module to.
# Like in Module it wont run.
# We usually use this for testing a code in this particular file.
if __name__ == "__main__":
    print("Hello")
