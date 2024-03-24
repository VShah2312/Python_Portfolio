"""
Question 3: Sort this list according to total marks and print it.
Here’s a student data with name, age, city, total marks.
"""

student_data = [
    ["Samantha", 18, "New York", 420],
    ["David", 25, "Los Angeles", 380],
    ["Sophie", 22, "Chicago", 390],
    ["Michael", 20, "Houston", 410],
    ["Liam", 19, "Phoenix", 430],
    ["Olivia", 21, "Philadelphia", 400],
    ["Daniel", 23, "San Antonio", 375],
]
# Here we changed the orignal list: don't do that
student_data.sort(key=lambda x: x[3])
print(student_data)

# Solution:
sorted_student_data = list(sorted(student_data, key=lambda x: x[3]))

print(sorted_student_data)
