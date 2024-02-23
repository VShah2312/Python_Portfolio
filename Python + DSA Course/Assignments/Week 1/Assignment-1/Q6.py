# Question 6:
games_played = int(input("Enter number of games played: "))
games_won = int(input("Enter number of games won: "))
games_lost = int(input("Enter number of games lost: "))
games_tie = games_played - games_lost - games_won
total_points = games_won * 4 + games_tie * 2
print(
    f"User played {games_played} games. Won {games_won} games, lost {games_lost} and {games_tie} games tied. Total points for the user is {total_points}"
)
