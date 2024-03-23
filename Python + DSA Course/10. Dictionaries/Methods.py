"""
Methods: 
"""

my_dict = {
    "vrunda": 75,
    "akul": 89,
    "muskan": 52,
}
# 1. .keys()
print(my_dict.keys())  # Returns list of keys.
# 2. .values()
print(my_dict.values())  # Returns list of values.
# 3. .items()
print(my_dict.items())  # Returns list of key-value tuples.
# 4. Len()
print(len(my_dict))  # Returns number of key-value pairs in the dict.
# 5. Clear:
# my_dict.clear()
# print(my_dict)  # -> {}
# # 6. Del
# del my_dict
# print(my_dict)  # NameError
# 7. .get() gives same output as print(my_dict["vrunda"]) #-> 75
print(my_dict.get("vrunda"))  # -> 75
print(
    my_dict.get("Vrrunda")
)  # -> None but print(my_dict["Vrrunda"]) -> will throw key error.

# 8. pop Here pop needs input
# print(my_dict.pop("Vrunda")) # KeyError
x = my_dict.pop("vrunda")
print(x)  # Here for pop we enter key and we get value.
print(my_dict)

# 9. update:
my_dict["sanjay"] = 92
my_dict["nihar"] = 28
print(my_dict)
# Here can append a dict and if key already exists, it will be updated.
# if key doesnt exist it will be added.
my_dict.update({"anirudh": 76, "vrunda": 56, "akul": 63})
print(my_dict)
