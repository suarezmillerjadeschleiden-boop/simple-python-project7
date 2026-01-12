# Import the random module to let the computer make a random choice
import random

# Print the title of the game
print("Rock Paper Scissors Game")

# Create a list of possible choices
choices = ["rock", "paper", "scissors"]

# Ask the user for their choice and convert it to lowercase
user_choice = input("Enter rock, paper, or scissors: ").lower()

# Let the computer randomly choose from the list
computer_choice = random.choice(choices)

# Show both choices
print("You chose:", user_choice)
print("Computer chose:", computer_choice)

# Check if both choices are the same
if user_choice == computer_choice:
    print("It's a tie!")

# Check all winning conditions for the user
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")

# If the input is valid but the user didn't win, they lose
elif user_choice in choices:
    print("You lose!")

# If the input is not valid
else:
    print("Invalid input.")
