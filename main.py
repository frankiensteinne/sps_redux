from art import logo
import random

# Dictionary containing game modes, descriptions, and winning combinations
game_data = {
    "Original": {
        "description": "Stone beats Scissors; Paper beats Stone; and Scissors beats Paper.",
        "winning_combinations": {"Stone": "Scissors", "Scissors": "Paper", "Paper": "Stone"},
    },
    "Reverse": {
        "description": "Scissors beats Paper, Paper beats Stone; and Stone beats Scissors.",
        "winning_combinations": {"Scissors": "Paper", "Paper": "Stone", "Stone": "Scissors"},
    },
    # Add more game modes here
}

# Global variables to track game statistics
current_mode = ""
number_of_games = 0
player_wins = 0
computer_wins = 0

def print_logo():
    """Prints the game logo."""
    print(logo)

def choose_game_mode(game_data):
    """
    Allows the player to choose a game mode.

    Parameters:
    - game_data (dict): A dictionary containing game modes, descriptions, and winning combinations.

    Returns:
    - str: The selected game mode.
    """
    print("Select a game mode:")
    for i, (mode, data) in enumerate(game_data.items()):
        print(f"Type {i} for {mode}")

    while True:
        selected_index = input("Input game mode index: ")

        if selected_index.isdigit() and 0 <= int(selected_index) < len(game_data):
            return list(game_data.keys())[int(selected_index)]
        else:
            print("Invalid input. Please enter a valid index.")

def determine_winner(player_choice, computer_choice, game_data):
    """
    Determines the winner based on the game mode and choices made by the player and computer.

    Parameters:
    - player_choice (str): The player's choice.
    - computer_choice (str): The computer's choice.
    - game_data (dict): A dictionary containing game modes, descriptions, and winning combinations.

    Returns:
    - str: The result of the round (win, lose, or draw).
    """
    if player_choice == computer_choice:
        return "It's a draw!"
    elif computer_choice == game_data[current_mode]["winning_combinations"][player_choice]:
        return "You win!"
    else:
        return "You lose!"

def game_and_win_tracker():
    """Displays the number of games played, player wins, and computer wins."""
    print(f"Number of games played: {number_of_games}")
    print(f"Player wins: {player_wins}")
    print(f"Computer wins: {computer_wins}")

def start_game():
    """
    Starts the Rock-Paper-Scissors game.

    Manages the main game loop, player input, computer choices, and game statistics.
    """
    global number_of_games, player_wins, computer_wins, current_mode

    print_logo()
    current_mode = choose_game_mode(game_data)
    print(game_data[current_mode]["description"])

    while True:
        player_choice = input("Choose Stone, Scissors, or Paper: ").title()
        if player_choice not in ["Stone", "Scissors", "Paper"]:
            print("Invalid choice. Please choose Stone, Scissors, or Paper.")
            continue

        computer_choice = random.choice(list(game_data[current_mode]["winning_combinations"].keys()))
        print(f"Computer chose {computer_choice}")

        result = determine_winner(player_choice, computer_choice, game_data)
        print(result)

        number_of_games += 1
        if "win" in result.lower():
            player_wins += 1
        elif "lose" in result.lower():
            computer_wins += 1

        game_and_win_tracker()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

    while True:
        player_choice = input("Choose Stone, Scissors, or Paper: ").title()
        if player_choice not in ["Stone", "Scissors", "Paper"]:
            print("Invalid choice. Please choose Stone, Scissors, or Paper.")
            continue

        computer_choice = random.choice(list(game_data[current_mode]["winning_combinations"].keys()))

        print(f"You chose- {player_choice}, Computer chose- {computer_choice}")

        result = determine_winner(player_choice, computer_choice, game_data)
        print(result)

        number_of_games += 1
        if "win" in result.lower():
            player_wins += 1
        elif "lose" in result.lower():
            computer_wins += 1

        game_and_win_tracker()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    start_game()
