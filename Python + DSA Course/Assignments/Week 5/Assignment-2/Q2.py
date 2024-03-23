"""
Question 2: Create a function named countChar which will accept a string as a
parameter. Create a dictionary having frequency of each character.
"""

from typing import Dict


def countChar(str) -> Dict:
    my_list = list(str)
    dict = {char: my_list.count(char) for char in my_list}
    return dict


print(countChar("heellloo"))
print(countChar("delhi delhi"))

# Solution:
from typing import Dict


def countChar_soln(string: str) -> Dict:
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


print(countChar_soln("delhi delhi"))
