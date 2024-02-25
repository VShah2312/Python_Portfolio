# Reverse the number provided.
# example 123 -> 321, 158296 -> 692851
# Doesnt work for any time we have zero in the number with this method.


def reverse(n: int) -> int | None:
    num = n
    reverse_number = 0
    while True:
        if num % 10 == 0:
            break
        last_digit = num % 10  # 123% 10 -> 3(last_digit)
        num = num // 10  # 123//10 -> 12
        reverse_number = reverse_number * 10 + last_digit
    return reverse_number


num: int = int(input("Enter a number not ending in 0: "))

print(reverse(num))

# Method 2 this will work for 10 multiples too but wont give answer in leading 0.


def reverse_2(n: int) -> int | str:
    num = n
    reverse_number = 0
    i = 1
    while i <= len(str(n)):
        last_digit = num % 10  # 123% 10 -> 3(last_digit)
        num = num // 10  # 123//10 -> 12
        reverse_number = reverse_number * 10 + last_digit
        i += 1
    return reverse_number


num: int = int(input("Enter a number: "))

print(reverse_2(num))


# trial
def reverse_3(n: int) -> int | None:
    num = n
    reverse_number = 0
    string = ""
    while num % 10 == 0:
        num = num // 10
        string += "0"
    while True:
        if num % 10 == 0:
            break
        last_digit = num % 10  # 123% 10 -> 3(last_digit)
        num = num // 10  # 123//10 -> 12
        reverse_number = reverse_number * 10 + last_digit
    return string + str(reverse_number)


num: int = int(input("Enter a number: "))

print(reverse_3(num))
