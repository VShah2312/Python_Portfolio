"""
Question 3:  Write a Python program to print a dictionary line by line.
"""

from typing import Dict


def function(my_dict: Dict):
    for k, v in my_dict.items():
        print(k)
        for i, j in v.items():
            print(f"{i}:{j}")


my_dict = {
    "Sam": {"M1": 89, "M2": 56, "M3": 89},
    "Suresh": {"M1": 49, "M2": 96, "M3": 89},
}
function(my_dict)
