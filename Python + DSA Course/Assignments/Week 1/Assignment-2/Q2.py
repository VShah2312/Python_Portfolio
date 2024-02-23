"""Question 2: A student will not be allowed to sit in exam if his/her attendance is less then 75%. Take two inputs from user
a. number of classes held.
b. number of classes attended.
Print percentage of class attended and print is student allowed to sit in exam or not."""

class_held: int = int(input("Enter number of classes held: "))
class_attnd: int = int(input("Enter number of classes attended: "))

attnd_percent = (class_attnd / class_held) * 100
print(f"Percentage of class attended is {attnd_percent} %")

if attnd_percent >= 75:
    print("You are allowed to sit in the exam.")
else:
    print("You are not allowed to sit in the exam.")
