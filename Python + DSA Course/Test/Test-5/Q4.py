"""
Question 4:  Create a dictionary that counts the frequency of words in a given
string. Ask string from user.
Input String: "The sun is shining and the weather is nice"
Output:
{
'The': 1,
'sun': 1,
'is': 2,
'shining': 1,
'and': 1,
'the': 1,
'weather': 1,
'nice': 1
}
"""


def frequency(string: str) -> dict:
    result = string.split()
    dictionary = {i: result.count(i) for i in result}
    return dictionary


my_string = "The sun is shining and the weather is nice"
print(frequency(my_string))
my_string_2 = "The cat and the dog played in the park The cat chased the dog"
print(frequency(my_string_2))


# Solution:
# Optimal Way
def wordFrequency(string: str):
    words = string.split()
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    return frequency_dict


frequency = wordFrequency("python is is a good python good python")
print(frequency)
