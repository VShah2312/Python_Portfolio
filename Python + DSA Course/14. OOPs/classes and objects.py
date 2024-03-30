"""
Classes and Objects: Can make any number of classes and objects. Also n number of methods.
"""


class Student:  # first letter of any class name has to be capital.
    # Intializing attributes.
    roll_no = 0
    name = ""
    gender = ""
    age = 0


s1 = Student()  # Creating s1 object. Like my_list=list()
s2 = Student()  # Creating s2 object.
s3 = Student()  # Creating s3 object.
s1.age = 19
s1.gender = "Male"
s1.name = "Anirudh"
s1.roll_no = 99
# print(s1)  # You can print an object but it doesnt give workable answers. It gives location of the object.
# You can print members/attributes of object.
# We are changing s1, we can see s2 is not affected.
print(s1.name, s1.age, s1.roll_no, s1.gender)
print(s2.name, s2.age, s2.roll_no, s2.gender)
