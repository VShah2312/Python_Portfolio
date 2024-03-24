"""
Question 2: 
"""

student_data = {
    "Ella": {"age": 20, "marks": [85, 78, 92, 89, 91]},
    "Max": {"age": 22, "marks": [79, 85, 88, 90, 87]},
    "Sophia": {"age": 21, "marks": [92, 95, 88, 85, 91]},
    "Liam": {"age": 23, "marks": [76, 80, 79, 82, 85]},
    "Ava": {"age": 20, "marks": [88, 92, 85, 90, 87]},
    "Noah": {"age": 22, "marks": [83, 85, 80, 86, 88]},
    "Emma": {"age": 21, "marks": [90, 87, 92, 88, 86]},
}
result = dict()
for k, v in student_data.items():
    result[k] = sum(v["marks"])

result_2 = sorted(result.items(), key=lambda x: x[1])
# Result_2 is tuple of key, value
print(result_2)

# Tuple unpacking
for k, v in result_2:
    print(f"{k} has scored {v}")

# Solution:

sorted_student_data = dict(
    sorted(student_data.items(), key=lambda x: sum(x[1]["marks"]))
)

for name, details in sorted_student_data.items():
    total_marks = sum(details["marks"])
    print(f"{name} has scored {total_marks}")
