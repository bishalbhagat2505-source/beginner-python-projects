import random
# ---------------- GET PLAYER CHOICE ----------------
def get_player_choice():
    while True:
        choice = input(
            "Choose Rock, Paper, or Scissor: "
        ).lower()
        # Validate input
        if choice in ["rock", "paper", "scissor"]:
            return choice.capitalize()
        print("Invalid input. Please try again.\n")


# ---------------- GET COMPUTER CHOICE ----------------
def get_computer_choice():
    options = ["Rock", "Paper", "Scissor"]
    return random.choice(options)

# ---------------- CHECK WINNER ----------------
def check_winner(player, computer):
    print(f"\nPlayer Choice   : {player}")
    print(f"Computer Choice : {computer}\n")
    # Draw condition
    if player == computer:
        return "It's a Draw!"
    # Rock conditions
    elif player == "Rock":
        if computer == "Scissor":
            return "You Win!"
        return "Computer Wins!"
    # Paper conditions
    elif player == "Paper":
        if computer == "Rock":
            return "You Win!"
        return "Computer Wins!"
    # Scissor conditions
    elif player == "Scissor":
        if computer == "Paper":
            return "You Win!"
        return "Computer Wins!"

# ---------------- MAIN GAME LOOP ----------------
def play_game():
    print("=" * 35)
    print(" ROCK PAPER SCISSOR GAME ")
    print("=" * 35)
    while True:
        # Get choices
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        # Show result
        result = check_winner(
            player_choice,
            computer_choice
        )
        print(result)
        # Replay option
        play_again = input(
            "\nDo you want to play again? (y/n): "
        ).lower()
        if play_again != "y":
            print("\nThanks for playing!")
            break
        print()

# ---------------- START GAME ----------------
play_game()