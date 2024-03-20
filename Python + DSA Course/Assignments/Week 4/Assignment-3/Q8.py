"""
Question 8: Ask a string from user. Print the string with first 2 letters and last 2
letters.
"""


def firstAndLast(my_str) -> str:
    if len(my_str) < 3:
        return "INVALID"
    result_1 = my_str[0:2]
    result_2 = my_str[-2::]
    return result_1 + result_2


print(firstAndLast("aeroplane"))
print(firstAndLast("ae"))


# Solution:
def printFirstAndLastTwoCh(string: str):
    if len(string) < 2:
        print("Not enough characters")
        return

    print(string[:2] + string[-2:])


printFirstAndLastTwoCh("code")
printFirstAndLastTwoCh("aeroplane")
printFirstAndLastTwoCh("c")
