"""
Sorting: 
"""

my_list = [["Anirudh", 76], ["Vandana", 26], ["Akul", 67], ["Sanjay", 92]]
print(my_list[0][1])
print(my_list[2][1])
print(my_list[3][-1])
print(my_list[-4][-1])

# my_list.sort()  # This sorts by ASCI value. Sort is only available for List. Changes the list.
# print(my_list)

# x = sorted(
#     my_list
# )  # This returns and doesnt change in the list. Sorted is available for all data type (Dict etc)
# print(x)

# my_list.sort(key=lambda x: x[1], reverse=True)
# print(my_list)


# x = sorted(my_list, key=lambda x: x[1])
# print(x)

my_details = [
    {"name": "Anirudh", "age": 67, "gender": "Male"},
    {"name": "Clara", "age": 52, "gender": "Female"},
    {"name": "Vandana", "age": 63, "gender": "Female"},
    {"name": "Amber", "age": 23, "gender": "Male"},
]

# This sort works as my_details is list of dict.
my_details.sort(key=lambda x: x["age"], reverse=True)
print(my_details)


# Alternate way
def abc(x):
    print(x)
    return x["age"]


# Here we  are not calling the function we are giving reference of the functions as key takes a function.
# You can see it displays each line of dict due to line 40 even though we are only using on reference in below query.
my_details.sort(key=abc, reverse=True)
print(my_details)
