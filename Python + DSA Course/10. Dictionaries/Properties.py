"""
Properties: 
    Dict are mutable.
    We use keys to access elements in dictionary.
"""

# Acess elements using key:
my_dict = {
    "vrunda": 75,
    "akul": 89,
    "muskan": 52,
    "nihar": True,
    "xyz": [1, 2, 3],
    "pratik": {"age": 14, "gender": "Male"},
    10: "pqr",
    55.56: 11,
    # [1, 2,3]: 10 # This will give error : TypeError
    (1, 2, 3): 10,  # This is tuple so wont give error.
}

print(my_dict["akul"])
# print(my_dict["Vrunda"]) # KeyError
