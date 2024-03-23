"""
Question 1: Write a Python script to sort (ascending and descending) a dictionary
by value.
"""

from typing import Dict

# def sortDict(dict:Dict):
#     result= []
#     for key,value in dict.items():
#         result= list[dict]
dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(sorted(dict.values()))
print(dict.fromkeys