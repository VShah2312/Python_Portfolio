# Power: function(base, exponent) -> b^e


# Functional:
def power(base: int, exponent: int) -> int:
    if exponent < 0 or type(exponent) != int:
        raise Exception("Invalid Value")
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


print(power(2, 2))
print(power(3, 2))
print(power(3, 1))
print(power(3, 0))
# print(power(3, -2))
