"""
Question 10: Python program to find the sum of all items in a dictionary.
"""

data = {"Vrunda": 23, "Charmi": 34, "Kavita": 56}

data_keys = [i for i in data.values()]
print(sum(data_keys))
