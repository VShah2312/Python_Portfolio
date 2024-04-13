"""
Task: Below are the steps:
Build a Number guessing game, in which the user selects a range.
Let's say User selected a range, i.e., from A to B, where A and B belong to Integer.
Some random integer will be selected by the system and the user has to guess 
that integer.
"""

import random


def game(n1: int, n2: int) -> str:
    if n1 > n2:
        print("Enter a valid range. num1 has to be less then num2.")
    else:
        i = n1
        list = []
        for i in range(i, n2 + 1):
            list.append(i)
            i += 1
        computer_choice = random.choice(list)
        n = int(input("Enter a guess: "))

        if computer_choice == n:
            return f"Computer chose {computer_choice}. Your guess is correct."
        return f"Computer chose {computer_choice}.Your guess is incorrect."


# num1, num2 = input("Enter a range of numbers seperated by ,: ").split(",")

# n1 = int(num1)
# n2 = int(num2)

print(game(5, 8))
