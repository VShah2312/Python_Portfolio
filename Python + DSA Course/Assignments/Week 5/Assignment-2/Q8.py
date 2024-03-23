"""
Question 8: Store name as a Key, and 5 marks in a List as a value in dictionary. Store
details of at least 5 students. Print only the total marks of every student in
ascending order.
"""

students = {
    "anirudh": {
        "physics": 12,
        "chemistry": 43,
        "maths": 1,
        "english": 76,
        "biology": 23,
    },
    "sanjay": {
        "physics": 78,
        "chemistry": 82,
        "maths": 80,
        "english": 43,
        "biology": 62,
    },
    "vrunda": {
        "physics": 13,
        "chemistry": 72,
        "maths": 32,
        "english": 89,
        "biology": 53,
    },
    "kavita": {
        "physics": 43,
        "chemistry": 12,
        "maths": 79,
        "english": 82,
        "biology": 85,
    },
    "charmi": {
        "physics": 54,
        "chemistry": 87,
        "maths": 72,
        "english": 86,
        "biology": 84,
    },
}
result = {}
for name, details in students.items():
    marks = details.values()
    result[name] = sum(marks)
print(sorted(result.values()))


# Solution:
students = {
    "Anirudh": [12, 43, 1, 76, 23],
    "Akul": [78, 82, 80, 43, 62],
    "Nihar": [13, 72, 32, 89, 53],
    "Anusha": [43, 12, 79, 82, 85],
    "Muskan": [54, 87, 72, 86, 84],
}


all_total_marks = []
for marks in students.values():
    total_marks = sum(marks)
    all_total_marks.append(total_marks)

all_total_marks.sort()

print(all_total_marks)
