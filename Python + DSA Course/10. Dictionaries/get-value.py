my_dict = {
    "vrunda": 75,
    "akul": 89,
    "muskan": 52,
}

print(my_dict.get("abc"))  # Return None
print(my_dict.get("abc", 0))  # If get cant find value it will return 0 instead of None
# By default its int.
