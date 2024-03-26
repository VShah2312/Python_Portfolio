"""
Question 6: Write a Python program to generate two strings from a given string. For
the first string, use the characters that occur only once, and for the
second, use the characters that occur multiple times in the said string.
"""


def splitFunction(my_string: str) -> None:
    result_1 = [i for i in my_string if my_string.count(i) == 1]
    result_2 = {i: my_string.count(i) for i in my_string if i not in result_1}.keys()
    string_1 = "".join(result_1)
    string_2 = "".join(result_2)
    print(f"{string_1=}")
    print(f"{string_2=}")


my_string = "aabbcceffgh"
splitFunction(my_string)
my_string = "heello"
splitFunction(my_string)


# Solution:
def generateStrings(input_string):

    char_freq = {}
    for ch in input_string:
        char_freq[ch] = char_freq.get(ch, 0) + 1
    # Part 1 contains single occurrence characters
    part1 = [key for (key, count) in char_freq.items() if count == 1]

    # Part 2 contains multiple occurrence characters
    part2 = [key for (key, count) in char_freq.items() if count > 1]

    return part1, part2


input = "heello"

s1, s2 = generateStrings(input)

print("".join(s1))
print("".join(s2))
