"""
List in dict: 

Output: 
    anirudh has scored total marks
    vrunda has scored total marks...
"""

students = {
    "anirudh": [54, 6, 32, 5, 66],
    "vrunda": [85, 25, 36, 14, 96],
    "sagar": [45, 12, 18, 78, 96],
    "charmi": [1, 2, 3, 4, 5],
}

# Method 1:
for k, v in students.items():
    print(f"{k} has score {sum(v)} marks")

# Method 2:
for k, v in students.items():
    sum_student = 0  # if we dont reset sum here, we would get cumulative marks.
    for i in v:
        sum_student += i
    print(f"{k} has score {sum_student} marks")

# Question avg marks of each students:

for k, v in students.items():
    average = sum(v) / len(v)
    print(f"{k} has score {average} marks")

# Question: Print total mark of the class

total = 0
for k, v in students.items():
    total += sum(v)
print(f"class total is {total}")

# Question: print the max and min marks of every students:
for k, v in students.items():
    print(f"{k} has score {max(v)} max marks and {min(v)} min marks")

# Question: print the average marks scored by whole class:

total = 0
length = 0
for k, v in students.items():
    total += sum(v)
    length += len(v)
print(f"class avg total marks  is {total/length}")

# Question: print maximum mark in that class and by who:
highest = 0
for k, v in students.items():
    max_student = max(v)
    if max_student > highest:
        name = k
        highest = max(v)
print(f"Highest marks in class {highest}, scored by {name}")
