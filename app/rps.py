import random
<<<<<<< Updated upstream
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
=======


VALID_OPTIONS = ["rock", "paper", "scissors"]

# ASK USER FOR AN INPUT (R/P/S)

user_choice = input("Please choose one of 'rock', 'paper', or 'scissors': ")
print("USER:", user_choice)

# VALIDATIONS

if user_choice not in VALID_OPTIONS:
    print("OOPS INVALID INPUT, PLEASE TRY AGAIN")
    # exit()
    quit()

# GENERATE RANDOM COMPUTER CHOICE

computer_choice = random.choice(VALID_OPTIONS)
print("COMP:", computer_choice)

# DETERMINE THE WINNER

print("TODO:", "DETERMINE WINNER")
>>>>>>> Stashed changes
