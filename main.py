import random

choices = {
    1: "Stone",
    2: "Paper",
    3: "Scissors"
}


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Stone" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Stone") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    print("Welcome to Stone, Paper, Scissors game!")
    
    
    print("Choose:")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissors")
    
    player_choice = int(input("Enter the number corresponding to your choice: "))
    
    if player_choice not in choices:
        print("Invalid choice! Please choose 1, 2, or 3.")
        return

   
    player_choice_str = choices[player_choice]
    
    
    computer_choice = random.randint(1, 3)
    computer_choice_str = choices[computer_choice]

    print(f"Your choice: {player_choice_str}")
    print(f"Computer's choice: {computer_choice_str}")
    
    result = determine_winner(player_choice_str, computer_choice_str)
    print(result)


play_game()
