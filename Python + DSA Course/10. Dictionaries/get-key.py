my_dict = {
    "vrunda": 75,
    "akul": 89,
    "muskan": 52,
}


user_input = input("Enter a key: ")

x = my_dict.get(user_input)
if x != None:
    print(x)
else:
    print("Key does not exist.")


# what if we have value None in dict:
my_dict = {"vrunda": 75, "akul": 89, "muskan": 52, "sanjay": None}

user_input = input("Enter a key: ")

x = my_dict.get(user_input)
if x != None:
    print(x)
else:
    print("Key does not exist.")

# Hence this is not best way. Because if we enter sanjay it will give Key doesnt exist. But key does exists.

# Best way:
user_input = input("Enter a key: ")

if user_input in my_dict:
    print(my_dict[user_input])
else:
    print("Key doesnt exist")
