class Student:
    # Method will take parameters while creating object.
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

    def __str__(self) -> str:
        # print(s1) instead of getting address of object that doesnt make sense.
        # we can choose what we want to return on print(s1)
        return f"Name = {self.name}, age = {self.age}"

    def __add__(self, other):
        # Lets you add objects. Here self is first obj. Other is second object.
        # Its completely on how to return the add
        # return self.age + other.age
        return self.name + other.name

    def __len__(self) -> int:
        # Its completely on how to return the len. You can hard code 15 if you want.
        # OR can return phone number.
        return self.phone_number

    """
    gt -> greater than 
    lt-> less than (not necessary to define its not gt)
    ge -> greater than equal to
    le->  less than equal to  (not necessary to define its not ge)
    eq- > equal to (not necessary to define, it goes to gt)
    ne -> not equal to  (not necessary to define its not eq)
    """

    def __gt__(self, other) -> bool:
        # lt is opposite of gt, so dont need to define unless we want different output.
        return self.age > other.age

    def __ge__(self, other) -> bool:
        # lt is opposite of gt, so dont need to define unless we want different output.
        return self.age >= other.age

    def __eq__(self, other) -> bool:
        # lt is opposite of gt, so dont need to define unless we want different output.
        return self.age == other.age

    # Similarly we can define others.

    def updateName(self) -> None:
        self.name = input("Enter new name: ")

    def updatePhoneNumber(self, new_number: int = 0) -> None:
        self.phone_number = new_number

    def display(self) -> None:
        """Display all the info related to the students/objects."""
        print(f"Roll no: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Age: {self.age}")
        print(f"Phone numbe:  {self.phone_number}")


s1 = Student(23, "Vrunda", "Female", 27, 1234567890)
s2 = Student(45, "Charmi", "Female", 80, 9034232233)
s3 = Student(92, "Kavita", "Female", 80, 4532313233)
print(s1 + s2)
print(len(s1))
print(s1 > s2)
print(s1 < s2)
print(s1 >= s2)
print(s1 <= s2)
print(s2 == s3)
print(s2 != s3)
