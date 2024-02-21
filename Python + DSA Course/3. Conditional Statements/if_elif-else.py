# Practice Problem:
# Ask user for 2 numbers and print which number is greater

# if- elif -else

# Example 1: Ask for a number from user. Print Positive, Negative or Zero

num: int = int(input("Enter a number: "))

if num < 0:
    print("Negative")
elif num == 0:
    print("Zero")
else:
    print("Positive")

# Example 2: Ask user a number. Print Yes if number is divisible by both 5 and 6.

num: int = int(input("Enter a number: "))

if num % 5 == 0 and num % 6 == 0:
    print("Yes")
else:
    print("No")

# Example 3: FOO-BAR
# Ask a number from user. If divisible 3 -> FOO, if divisible by 5 -> BAR, if divisible by both -> FOOBAR and neither -> FOOFOOBARBAR

num: int = int(input("Enter a number: "))
i = "FOO"
j = "BAR"

if num % 3 == 0 and num % 5 == 0:
    print(i + j)
elif num % 3 == 0:
    print(i)
elif num % 5 == 0:
    print(j)
else:
    print(i * 2 + j * 2)

# Example 4: Ask grade from a user. 91-100-> A, 81-90-> B, 71-80 -> C, 61-70->D 0-60 ->Fail

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
