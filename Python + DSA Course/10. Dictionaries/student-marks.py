"""
Question 1: 
anirudh has scored total marks 
sanjay has scored total marks 

Question 2: 
anirudh has scored percentage 
sanjay has scored percentage 
"""

students = {
    "anirudh": {"physics": 58, "chemistry": 45, "maths": 11, "english": 99},
    "sanjay": {"physics": 65, "chemistry": 85, "maths": 36, "english": 74},
    "vrunda": {"physics": 23, "chemistry": 96, "maths": 90, "english": 85},
}
# Method 1:
for name, marks in students.items():
    total_marks = (
        marks["physics"] + marks["chemistry"] + marks["maths"] + marks["english"]
    )
    print(f"{name} has scored {total_marks} marks")

# Question 1:
for name, details in students.items():
    print(f"{name} has scored {sum(details.values())} marks")

# Question 2:
for name, details in students.items():
    marks = details.values()
    percentage = (sum(marks) / (len(marks) * 100)) * 100
    print(f"{name} has scored {percentage} %")
