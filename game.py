import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = ["rock", "paper", "scissors"]
game_logo = [rock, paper, scissors]
print("This game is created by Syed Sanhad\n")
# Take input
ui = input("Enter your choice: 'ROCK', 'PAPER', or 'SCISSORS': ").lower()

# Validate input
if ui not in game:
    print("WRONG INPUT")
else:
    # Get user and computer choices
    computer_choice = random.choice(game)
    user_index = game.index(ui)
    computer_index = game.index(computer_choice)

    # Display choices and logos
    print(f"\nYou chose: {ui}\n{game_logo[user_index]}")
    print(f"Computer chose: {computer_choice}\n{game_logo[computer_index]}")

    # Decide winner
    if ui == computer_choice:
        print("Result: It's a draw!")
    elif (ui == "rock" and computer_choice == "scissors") or \
         (ui == "scissors" and computer_choice == "paper") or \
         (ui == "paper" and computer_choice == "rock"):
        print("Result: You win!")
    else:
        print("Result: Computer wins!")
