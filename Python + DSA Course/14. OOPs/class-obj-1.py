class Student:
    roll_no = 0
    name = ""
    gender = ""
    age = 0

    def selfInfo(self):
        self.roll_no = int(input("Eneter roll no: "))
        self.name = input("Eneter name: ")
        self.gender = input("Eneter gender: ")
        self.age = int(input("Eneter age: "))
        phone_number = int(input("Enter a phone number: "))  # local variable.
        self.phone_number = int(input("Enter a phone number: "))  # global in class
        # Here we are overwriting roll_no, name, gende, age but phone number is new variable.
        # So we dont need to give defaul value.
        # So we remove line 2-5 if we dont want to give default value.

    def display(self):  # self is mandatory here
        # Here self implies object that you are calling.
        # it looks like paramter but here we dont need to enter it.
        # Display is method here as its specific to Student class.
        print(f"Roll no: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Age: {self.age}")
        print(f"Phone numbe:  {self.phone_number}")


s1 = Student()
# s2 = Student()
# s1.age = 19
# s1.gender = "Male"
# s1.name = "Anirudh"
# s1.roll_no = 99
# Instead we can create a function that will take inputs
s1.selfInfo()
# If you want to set values for another object.
# s2.selfInfo()
s1.display()
# s2.display()


# As human being we can forget to run selfInfo before display
# We would like to set value minute we create object
# In this case we are using special method (Dundar method) __intit__
# __Init__ is like constructor (method that run as soon as object is created)
# Constructor basically allocates/reserves memory when object is created.
# This is for atributes that you would like to get some specific value mandatorily.


class Student:
    """
    Create an object of Student with various attributes and features.
    """

    def __init__(
        self, roll_no: int, name: str, gender: str, age: int = 0, phone_number: int = 0
    ) -> None:
        self.roll_no = roll_no
        self.name = name
        self.gender = gender
        self.age = age
        self.phone_number = phone_number

    # OR
    # Keep in mind init is also function, so it can also take parameters.
    # In above method it will take parameters while creating object.

    # def __init__(self) -> None:
    #     self.roll_no = int(input("Eneter roll no: "))
    #     self.name = input("Eneter name: ")
    #     self.gender = input("Eneter gender: ")
    #     self.age = int(input("Eneter age: "))
    #     self.phone_number = int(input("Enter a phone number: "))

    def updateName(self) -> None:
        self.name = input("Enter new name: ")

    def updatePhoneNumber(self, new_number=0) -> None:
        self.phone_number = new_number

    def display(self):
        """Display all the info related to the studnet."""
        print(f"Roll no: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Age: {self.age}")
        print(f"Phone numbe:  {self.phone_number}")


s1 = Student()
s1.display()
s1.updatePhoneNumber(9998582)
s1.updateName()
print(s1.__doc__)  # -> None Gives information about class you have mentioned.
print(s1.display.__doc__)  # Give information about display method.
# Display any information mentioned in doc string in the very begining.
