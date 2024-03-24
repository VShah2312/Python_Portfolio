"""
Question 5: Here’s a student data. The first 3 elements are marks of student. Sort
this list and print it.
"""

student_data = [
    [78, 92, 85, "Alice"],
    [82, 79, 81, "Bob"],
    [92, 88, 85, "Charlie"],
    [80, 79, 82, "Diana"],
    [92, 85, 90, "Eva"],
    [85, 80, 86, "Frank"],
    [87, 92, 88, "Gina"],
]
result = []
for i in student_data:
    sum = 0
    for j in range(0, 3):
        sum += i[j]
    result.append((i[3], sum))

result.sort(key=lambda x: x[1])

for name, total in result:
    print(f"{name} has scored {total}")
