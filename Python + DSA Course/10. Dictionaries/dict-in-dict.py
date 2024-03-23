"""
Dict-in-dict: 
"Anirudh": {"age": 67, "gender": "Male"}, This is valid
"Anirudh": {"age": 67, "age": 47},  This is  not valid as age is not unique in value dict 
"""

students = {
    "Anirudh": {"age": 67, "gender": "Male"},  # This is valid
    "Clara": {"age": 52, "gender": "Female"},
    "Vandana": {"age": 63, "gender": "Female"},
    "Amber": {"age": 23, "gender": "Male"},
}

"""
Output: 
anirudh has age = 66
samjay has age = 11 """
for name, details in students.items():  # details is a dict.
    print(f"{name} has age = {details['age']}")


students = {
    "Anirudh": {"age": 67, "gender": "Male"},  # This is valid
    "Clara": {"gender": "Female"},
    "Vandana": {"age": 63, "gender": "Female"},
    "Amber": {"age": 23, "gender": "Male"},
}
# for name, details in students.items():
#     print(f"{name} has age = {details['age']}") # This will give KeyError for Clara.

for name, details in students.items():
    if "age" in details.keys():
        print(f"{name} has age = {details['age']}")
    else:
        print(f"{name} has no age. ")
