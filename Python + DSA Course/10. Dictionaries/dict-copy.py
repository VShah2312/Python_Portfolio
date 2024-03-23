my_dict = {
    "vrunda": 75,
    "akul": 89,
    "muskan": 52,
}

# Shallow copy
new_dict = my_dict.copy()
new_dict["anirudh"] = 85
print(my_dict)
print(new_dict)

"""
In case one of our value has list. 
When we make copy list will have same reference id 
Hence if we make change in that list, it will change in new_dict as well
Thus in order to avoid it we will need to make deep copy. 
"""
