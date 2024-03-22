"""
Dictionary: 
    1. key - value pairs. More like hash map. 
    2. Key has to unique. Only immutable data type
    3. Value/ value that can be repeated. Can be any data type
    4. Mutable and order is maintained but we cant access using indexs.
    5. Comma at end can change the format of the view of dictionary. Without comma it will show in one line. 
    6. We can't update keys (as they are immutable) but we can update values.
    7. If key exist it update it, if keys doesnt exists it will add the key.  
"""

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
print(my_dict)
print(type(my_dict))
