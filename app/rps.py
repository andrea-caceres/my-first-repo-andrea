import random
valid_choices = ["rock", "paper", "scissors"]
user_choice = input("please choose an option ('rock', 'paper', or 'scissors'):").strip().lower()

#input validation
while user_choice not in valid_choices:
    print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
    user_choice = input("Please choose an option ('rock', 'paper', or 'scissors'): ").strip().lower()

print(f"Option chosen: '{user_choice}'")

#computer choice
computer_choice = random.choice(valid_choices)
print(f"Computer choice: '{computer_choice}'")

#game
if user_choice == computer_choice:
    result = "It's a tie! Try again"
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    result = f"You win! "
else:
    result = "Computer wins!"

print(result)
print("Thanks for playing.")