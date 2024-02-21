# Rock, Paper, Scissors.

import random

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
c = computer_choice.lower()

user_choice: str = input("Enter your choice from rock, paper, scissors: ")
u = user_choice.lower()

if u != "rock" and u != "paper" and u != "scissors":
    print("Invalid input!")
elif c == u:
    print(f"Tie. Try again! Computer chose {c}.")
elif c == "rock" and u == "paper":
    print(f"You win! Computer chose {c}.")
elif c == "paper" and u == "scissors":
    print(f"You win! Computer chose {c}.")
elif c == "scissors" and u == "rock":
    print(f"You win! Computer chose {c}.")
else:
    print(f"You lost. Computer chose {c}.")
