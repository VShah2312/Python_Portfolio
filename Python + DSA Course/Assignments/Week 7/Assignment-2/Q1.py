# Question 1:


class Student:
    def __init__(
        self, name: str = "", age: int = 0, gender: str = "", marks: list = []
    ) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.marks = marks

    def displayAllInfo(self) -> None:
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Marks: {self.marks}")

    def displayOnlyMarks(self) -> None:
        return self.marks

    def getTotal(self) -> float | int:
        return sum(self.marks)

    def getMax(self) -> float | int:
        return max(self.marks)

    def getMin(self) -> float | int:
        return min(self.marks)

    def getAvg(self) -> float | int:
        total = sum(self.marks)
        subjects = len(self.marks)
        return round(total / subjects, 2)

    def addMark(self, mark: int) -> list:
        (self.marks).append(mark)
        return self.marks

    def removeMark(self, mark: int = -1) -> list | str:
        try:
            (self.marks).remove(mark)
            return self.marks
        except:
            return "Marks not in the object."


# Creating a student object:
student1 = Student("Vrunda Shah", 27, "Female", [85, 90, 95, 80])

# Display all information about the student:
student1.displayAllInfo()

# Display only the marks obtained by the student:
print(student1.displayOnlyMarks())

# Get total marks obtained by the student:
total_marks = student1.getTotal()
print("Total Marks: ", total_marks)

# Get maximum marks obtained by the student:
max_marks = student1.getMax()
print("Maximum Marks: ", max_marks)

# Get minimum marks obtained by the student:
min_marks = student1.getMin()
print("Minimum Marks: ", min_marks)

# Get average marks obtained by the student:
avg_marks = student1.getAvg()
print("Average Marks: ", avg_marks)

# Add a new mark to the list:
print(student1.addMark(87))

# Remove the last mark from the list:
print(student1.removeMark(57))
print(student1.removeMark(87))
