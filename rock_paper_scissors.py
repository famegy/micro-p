import random
print("Rock Paper Scissors Game")

computer_wins = 0
user_wins = 0
draw_counts =0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("make your guess(Rock, Paper, Scissors and Q to quit): ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("Please choose the correct option")
        continue

    computer_choice = random.choice(options)
    if user_input == computer_choice:
        print("It's a draw!")
        draw_counts += 1
    elif user_input == "rock" and computer_choice == "scissors":
        user_wins += 1
        print("You win!")
    elif user_input == "paper" and computer_choice == "rock":
        user_wins += 1
        print("You win!")
    elif user_input == "scissors" and computer_choice == "paper":
        user_wins += 1
        print("You win!")

    else:
        print("Computer won!")
        computer_wins += 1

print("You won", user_wins, "times")
print("Computer won", computer_wins, "times")
print("It's a draw", draw_counts, "times")