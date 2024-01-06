import random

# Function to determine the winner
def determine_winner(player, computer):
    print(f"Your choice: {player}")
    print(f"Computer 1's choice: {computer[0]}")
    print(f"Computer 2's choice: {computer[1]}")
    print(f"Computer 3's choice: {computer[2]}")

    if player in computer:
        print("It's a tie!")
    else:
        if (player == 'rock' and 'scissors' in computer) or \
           (player == 'paper' and 'rock' in computer) or \
           (player == 'scissors' and 'paper' in computer):
            print("Congratulations! You win!")
        else:
            print("Computers win!")

# Function to simulate computer choices
def computer():
    choices = ['rock', 'paper', 'scissors']
    return [random.choice(choices) for _ in range(3)]

# Function to run the game
def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    print("Choose: rock, paper, or scissors.")
    player_choice = input("Your choice: ").lower()

    if player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose: rock, paper, or scissors.")
        return

    comp_choices = computer()
    determine_winner(player_choice, comp_choices)

# Run the game
play_game()
