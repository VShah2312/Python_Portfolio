"""
Question 7: Convert a list of Tuples into Dictionary
Input: [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25),("ashish", 30)]
Output: {'akash': [10],'gaurav': [12],'anand': [14],'ashish': [30],'akhil': [25],'suraj': [20]}
Input: [('A', 1), ('B', 2), ('C', 3)]
Output: {'B': [2],'A': [1],'C': [3]}
"""


def tupleToDict(my_list: list) -> dict:
    my_dict = {}
    for k, v in my_list:
        my_dict[k] = [
            v,
        ]
    return my_dict


my_list = [("A", 1), ("B", 2), ("C", 3)]
print(tupleToDict(my_list))
my_list = [
    ("akash", 10),
    ("gaurav", 12),
    ("anand", 14),
    ("suraj", 20),
    ("akhil", 25),
    ("ashish", 30),
]
print(tupleToDict(my_list))


def convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di


# Driver Code
tups = [
    ("akash", 10),
    ("gaurav", 12),
    ("anand", 14),
    ("suraj", 20),
    ("akhil", 25),
    ("ashish", 30),
]
dictionary = {}
print(convert(tups, dictionary))
