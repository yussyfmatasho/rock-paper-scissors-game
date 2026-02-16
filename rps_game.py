import random  # Importing random module to let computer choose randomly

# Intro to the game
print("Welcome to Rock–Paper–Scissors!")  # Greeting message
print("Type: rock, paper, or scissors")   # Instructions for the player
print("Type: quit to exit the game")      # Command to exit the game
print("Let’s begin!")

# List of valid commands
commands = ["rock", "paper", "scissors"]  # Possible choices in the game

# Scoreboard variables
total_games = 0      # Counts total number of games played
computer_wins = 0    # Counts how many times computer won
player_wins = 0      # Counts how many times player won
draws = 0            # Counts number of draws

# Dictionary that defines winning rules
# Key beats value (rock beats scissors, etc.)
wins_against = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

# Main game loop (runs forever until player types quit)
while True:

    # Player input (converted to lowercase to avoid case problems)
    player_choice = input("Your choice: ").strip().lower()

    # If player wants to quit — break the loop
    if player_choice == "quit":
        break

    # Check if input is invalid
    if player_choice not in commands:
        print("Invalid input! Please type rock, paper, scissors, or quit.")
        continue  # Skip the rest and ask again

    # Computer randomly chooses from commands list
    computer_choice = random.choice(commands)
    print("Computer chose:", computer_choice)

    # Increase total games counter
    total_games += 1

    # Check for draw
    if player_choice == computer_choice:
        print("Draw!")
        draws += 1

    # Check if player wins
    elif wins_against[player_choice] == computer_choice:
        print("You won! Nice game!")
        player_wins += 1

    # Otherwise computer wins
    else:
        print("Computer won! Nice try!")
        computer_wins += 1

    # Print updated score after each round
    print("Your score is", player_wins)
    print("Computer's score is", computer_wins)
    print("Draws are", draws)
    print("Total games are", total_games)
    print("Type rock/paper/scissors to play again, or quit to exit.")

# Final results after quitting
print("Final score:")
print("Your score is", player_wins)
print("Computer's score is", computer_wins)
print("Total games are", total_games)
print("Thank you for the game!")