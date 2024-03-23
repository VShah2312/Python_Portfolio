"""
Question 11: Write a Python program to sort a dictionary by the length of its keys.
Original dictionary: {'apple': 2,'banana': 3,'pear': 4,'orange': 5}
Sorted dictionary by key length:{'pear': 4,'apple': 2,'banana': 3,'orange': 5}
"""

my_dict = {"apple": 2, "banana": 3, "pear": 4, "orange": 5}

# Ascending order by length of its keys:
print(dict(sorted(my_dict.items(), key=lambda x: len(x[0]))))

# Ascending order by length of its keys:
print(dict(sorted(my_dict.items(), key=lambda x: len(x[0]), reverse=True)))
