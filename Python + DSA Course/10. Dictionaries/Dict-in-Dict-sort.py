students = {
    "Anirudh": {"age": 67, "gender": "Male"},
    "Clara": {"age": 52, "gender": "Female"},
    "Vandana": {"age": 63, "gender": "Female"},
    "Amber": {"age": 23, "gender": "Male"},
}
# Give list of key-value tuples.
print(students.items())

# Dictionary doesnt have indexing but items does.
# x[0] is keys, x[1] means values
x = dict(sorted(students.items(), key=lambda x: x[1]["age"]))
print(x)

# a=("age", 55)
# print(dict(a)) # Throws error

# but this will works as we have tuple of key value pair. Thus we can convert to dictionary.
a = [("age", 55), ("xyz", 45)]
print(dict(a))


# Question: Sort below dict on bases of total marks.
# x[1]["marks"]= [2, 3, 11, 24, 55] and similiar.
students = {
    "anirudh": {"age": 66, "gender": "Male", "marks": [2, 3, 11, 24, 55]},
    "sanjay": {"gender": "Male", "age": 32, "marks": [54, 76, 12, 232, 11, 65]},
    "vandana": {"age": 53, "gender": "Female", "marks": [65, 77, 33]},
}
x = dict(sorted(students.items(), key=lambda x: sum(x[1]["marks"])))
print(x)


# Question: sort by last value in marks:
students = {
    "anirudh": {"age": 66, "gender": "Male", "marks": [2, 3, 11, 24, 55]},
    "sanjay": {"gender": "Male", "age": 32, "marks": [54, 76, 12, 232, 11, 65]},
    "vandana": {"age": 53, "gender": "Female", "marks": [65, 77, 33]},
}
x = dict(sorted(students.items(), key=lambda x: x[1]["marks"][-1]))
print(x)
