"""
Question 11: 
"""

data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

# Sort the list of dictionaries by 'age'
sorted_data = sorted(data, key=lambda x: x["age"])


data.sort(key=lambda x: x["age"])
print(sorted_data)
print(data)
