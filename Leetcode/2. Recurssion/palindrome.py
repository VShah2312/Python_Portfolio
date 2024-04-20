# Check if provided string is palindrome, using recurssion


def function(my_string: str, i: int) -> bool:
    if i > len(my_string) // 2:
        return True
    if my_string[i] != my_string[len(my_string) - 1 - i]:
        return False
    return function(my_string, i + 1)


print(function("mom", 0))
print(function("nitin", 0))
