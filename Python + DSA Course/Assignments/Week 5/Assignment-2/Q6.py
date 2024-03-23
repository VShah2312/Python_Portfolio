"""
Question 6: Write a Python program to create a dictionary of keys x, y, and z where
each key has as value a list from 11-20, 21-30, and 31-40 respectively.
Access the fifth value of each key from the dictionary.
"""


def fifthelement(my_dict):
    for k, v in my_dict.items():
        print(v[4])


dict = {
    "x": [i for i in range(11, 20)],
    "y": [i for i in range(21, 30)],
    "z": [i for i in range(31, 40)],
}

print(fifthelement(dict))
