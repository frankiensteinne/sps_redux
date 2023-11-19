from art import logo
from random import randint

GAME_MODES = {
    "Original":"Stone beats Scissors; Paper beats Stone; and Scissors beats Paper.",
    "Reverse":"Scissors beats Paper, Paper beats Stone; and Stone beats Scissors."
}

current_mode =""

number_of_games = 0
player_wins = 0
computer_wins = 0

# print(logo)
# player_name = input("Input your name.\n").title()

def choose_game_mode(game_modes):
    """
    Allows the player to choose a game mode.

    Parameters:
    -game_modes (dict): A dictionary containing game modes and their descriptions.

    Returns:
    -str: The selected game mode.
    """

    # Display available game modes to the player
    for i, mode in enumerate(game_modes):
        print(f"Type {i} to play {mode}")

    # Get user input for the selected game mode index
    while True:
        selected_index = input("Input game mode index: ")

        # Check if the input is a valid index
        if selected_index.isdigit() and 0 <= int(selected_index) < len(game_modes):
            return list(game_modes.keys())[int(selected_index)]
        else:
            print("Invalid input. Please enter a valid index.")

# Determine Winner Function

# Game and Win Tracker Function

# Continue or End Game Function


current_mode = choose_game_mode(GAME_MODES)
print(f"Selected game mode: {current_mode}")