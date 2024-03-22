"""
Question: Can I update a key? No, keys are immutable. 
    We can update values. Order is mainted in dict. 
    If key is repeated, dict will keep the latest value but keep it in position where key first shows up.

    Delete: you cant delete just values.
        del my_dict[key] -> deletes key value order pair. 

    Dict: behaves like set, as we have unique key-value. Value acess in set and dict, is much faster then list and tuples.
        And as set is unordered. Dict is ordered. So we can treat dict as ordered set. 
"""

my_dict = {"vrunda": 75, "akul": 89, "muskan": 52, "akul": 34}
print(my_dict)
my_dict["vrunda"] = 100  # Updates value if key exists
my_dict["nihar"] = 45  # Adds to dict if key doesnt exists.
print(my_dict)


del my_dict["akul"]
print(my_dict)
