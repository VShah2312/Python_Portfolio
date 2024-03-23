"""
Question 7: Store name as a Key, and 5 marks in a List as a value in dictionary. Store
details of at least 5 students. Print the total marks with percentage of each
and every student.
"""

students = {
    "anirudh": {
        "physics": 58,
        "chemistry": 45,
        "maths": 11,
        "english": 99,
        "biology": 85,
    },
    "sanjay": {
        "physics": 65,
        "chemistry": 85,
        "maths": 36,
        "english": 74,
        "biology": 88,
    },
    "vrunda": {
        "physics": 23,
        "chemistry": 96,
        "maths": 90,
        "english": 85,
        "biology": 25,
    },
    "charmi": {
        "physics": 19,
        "chemistry": 92,
        "maths": 52,
        "english": 36,
        "biology": 75,
    },
    "kavita": {
        "physics": 52,
        "chemistry": 68,
        "maths": 41,
        "english": 80,
        "biology": 86,
    },
}


for name, details in students.items():
    marks = details.values()
    percentage = (sum(marks) / (len(marks) * 100)) * 100
    print(f"{name} has scored {sum(marks)} total marks and {percentage:.2f} %")


# Solution:
def calculatePercentage(total_marks):
    return (total_marks / 500) * 100


students = [
    {"name": "Anirudh", "marks": [12, 43, 1, 76, 23]},
    {"name": "Akul", "marks": [78, 82, 80, 43, 62]},
    {"name": "Nihar", "marks": [13, 72, 32, 89, 53]},
    {"name": "Anusha", "marks": [43, 12, 79, 82, 85]},
    {"name": "Muskan", "marks": [54, 87, 72, 86, 84]},
]

for student in students:
    total_marks = sum(student["marks"])
    percentage = calculatePercentage(total_marks)
    print(
        f"Name: {student['name']}, Total Marks: {total_marks}, Percentage: {percentage:.2f}%"
    )
