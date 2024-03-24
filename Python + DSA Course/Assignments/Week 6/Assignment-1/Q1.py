"""
Question 1: Display the name of student and total marks in ascending order.
"""

student_data = {
    "Alice": [85, 90, 88, 92, 89],
    "Bob": [78, 82, 79, 81, 80],
    "Charlie": [92, 95, 88, 85, 91],
    "Diana": [76, 80, 79, 82, 85],
    "Eva": [88, 92, 85, 90, 87],
    "Frank": [83, 85, 80, 86, 88],
    "Gina": [90, 87, 92, 88, 86],
}
result = dict()
for k, v in student_data.items():
    result[k] = sum(v)

result_2 = sorted(result.items(), key=lambda x: x[1])
# Result_2 is tuple of key, value
print(result_2)

# Tuple unpacking
for k, v in result_2:
    print(f"{k} has scored {v}")

# Solution:
sorted_student_data = dict(sorted(student_data.items(), key=lambda x: sum(x[1])))

for name, marks in sorted_student_data.items():
    total_marks = sum(marks)
    print(f"{name} has scored {total_marks}")
