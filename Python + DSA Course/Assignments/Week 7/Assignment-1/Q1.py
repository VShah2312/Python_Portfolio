"""
Question 1:Create a class called Employee with attributes such as name, age,
gender, and phone number. Implement a constructor to initialize these
attributes.
Include methods to calculate monthly and yearly salary based on hourly
rate and hours worked. Ask hourly rate and hours worked inside the
method (local variable).
Create 2 objects and check your code.
"""


class Employee:
    """
    Create an object of Employee with various attributes and features.
    """

    def __init__(
        self, name: str = "", age: int = 0, gender: str = "", phone_number: int = 0
    ) -> None:
        pass

    def weekly_salary(self) -> float:
        """Calculates weekly salary of an employee."""
        hourly_rate: float = float(input("Enter employee's hourly rate: "))
        hours_worked: float = float(input("Enter employee's hours worked: "))
        weekly_pay = hourly_rate * hours_worked
        return weekly_pay

    def monthly_salary(self) -> float:
        """Calculates weekly salary of an employee."""
        hourly_rate: float = float(input("Enter employee's hourly rate: "))
        hours_worked: float = float(input("Enter employee's hours worked: "))
        weekly_pay = hourly_rate * hours_worked
        monthly_pay = weekly_pay * 4
        return monthly_pay

    def yearly_salary(self) -> float:
        """Calculates weekly salary of an employee."""
        hourly_rate: float = float(input("Enter employee's hourly rate: "))
        hours_worked: float = float(input("Enter employee's hours worked: "))
        weekly_pay = hourly_rate * hours_worked
        yearly_pay = weekly_pay * 54
        return yearly_pay


employee_1 = Employee("Vrunda", 27, "Female", 6036740027)
print(employee_1.weekly_salary())
