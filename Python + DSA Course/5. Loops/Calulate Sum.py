# Constantly keep asking for an input from user, break the loop if 0 is entered. Find sum of all the entered numbers.
total = 0
while True:
    # Condition is always true, so we will need to use break to get out of the loop.
    num: int = int(input("Enter a number:"))
    # This keep asking for input as long as loop is running.
    if num == 0:
        break
    total += num
print(f"total = {total}")


total = 0
while True:
    num: int = int(input("Enter a number:"))
    total += num  # Position of this matters.
    # With this is it will add number to the total and then break.
    if num == 5:
        break
print(f"total = {total}")
