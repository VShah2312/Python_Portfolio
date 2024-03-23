"""
Question 10: Write a Python program to sort a dictionary by its keys in ascending
order.
Original dictionary: {'b': 2,'a': 1,'c': 3}
Sorted dictionary by keys:{'a': 1,'b': 2,'c': 3}
"""

my_dict = {"b": 2, "a": 1, "c": 3}

# Ascending order by keys:
print(dict(sorted(my_dict.items())))

# Descending order by keys:
print(dict(sorted(my_dict.items(), reverse=True)))
