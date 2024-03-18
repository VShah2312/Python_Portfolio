""" 
Question 5: Write a Python code to find the occurrence of each element in a list
and print the element with the highest occurrence.
"""

a = [54, 14, 11, 12, 54, 14, 14, 54, 11, 54, 11, 11, 11]
keys = []
value = []
for val in a:
    if val not in keys:
        keys.append(val)
        value.append(a.count(val))
        print(f"{val}: {a.count(val)} times")
index = value.index(max(value))
print(
    f"The element with the highest occurence is: {keys[index]} ({value[index]} times)"
)


def my_function(a, b):
    return a + b


x = my_function(5, 6)
