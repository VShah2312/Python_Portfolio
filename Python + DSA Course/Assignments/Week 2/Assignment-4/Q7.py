"""
Question 7: Keep asking numbers from user until the user enters 0. Then display
the average of all numbers.
"""

count = 0
sum = 0
average = 0
while True:
    n: int = int(input("Enter a number (enter 0 to finish): "))
    if n == 0:
        break
    count += 1
    sum += n
average = sum / count
print(f"The average of the entered numbers is: {average}")
