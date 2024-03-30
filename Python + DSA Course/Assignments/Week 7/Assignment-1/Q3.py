"""
Question 3: Employee Class with Performance Evaluation
Attributes:
name: Name of the employee.
age: Age of the employee.def
gender: Gender of the employee.
phone: Phone number of the employee.
salary: Salary of that employee

Methods:
__init__(self, name, age, gender, phone,salary): Constructor method to
initialize the employee object with name, age, gender, and phone number,
salary attributes.
change_salary(self): Method that asks within the new salary and updates
the salary of that employee
display_details(self): Method to display all details of the employee,
including name, age, gender, phone number, salary.
"""


class Employee:
    """
    Create an object of Employee with various attributes and features.
    """

    def __init__(
        self,
        name: str = "",
        age: int = 0,
        gender: str = "",
        phone: int = 0,
        salary: int = 0,
    ) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.salary = salary

    def change_salary(self) -> None:
        """Updates employee object salary."""
        new_salary = int(input("Enter new salary: "))
        self.salary = new_salary

    def display_details(self) -> None:
        """Displays employee details."""
        print(f"{self.name =}")
        print(f"{self.age =}")
        print(f"{self.gender =}")
        print(f"{self.phone =}")
        print(f"{self.salary =}")


employee_1 = Employee("Vrunda Shah", 27, "Female", 6036740027, 2500)
employee_1.display_details()
employee_1.change_salary()
employee_1.display_details()
