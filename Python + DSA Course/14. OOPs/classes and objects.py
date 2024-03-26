"""
Classes and Objects: Can make n number of classes. 
"""


class Student:  # first letter of any class name has to be capital.
    roll_no = 0
    name = ""
    gender = ""
    age = 0


s1 = Student()  # s1 is an object here
s2 = Student()  # s1 is an object here
s3 = Student()  # s1 is an object here
s1.age = 19
s1.gender = "Male"
s1.name = "Anirudh"
s1.roll_no = 99
# print(s1)  # You cant print an object
print(s1.name, s1.age, s1.roll_no, s1.gender)
print(s2.name, s2.age, s2.roll_no, s2.gender)
