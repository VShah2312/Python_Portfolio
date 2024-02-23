# Question 4:Ask grade from a user. 91-100-> A, 81-90-> B, 71-80 -> C, 61-70->D 0-60 ->Fail

grade: int = int(input("Enter your marks: "))

if 91 <= grade <= 100:
    print("A")
elif 81 <= grade <= 90:
    print("B")
elif 71 <= grade <= 80:
    print("C")
elif 61 <= grade <= 70:
    print("D")
elif 0 <= grade <= 60:
    print("Fail")
else:
    print("Invalid marks, please enter marks between 0 and 100")
