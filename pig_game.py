import random


def roll_die():
    min_value = 1
    max_value = 6
    roll_value = random.randint(min_value, max_value)
    return roll_value


while True:
    players = input("enter the number of players (2-4): ")

    if players.isdigit():
        players = int(players)

        if 2 <= players <= 4:
            break
        else:
            print("Players must be 2-4 ")
    else:
        print("Invalid input!")


max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        current_score = 0

        while True:
            print("\n Player ", player_idx + 1, "turn to play")
            start_roll = input("Would you like to roll the dice (y) ").lower()

            if start_roll != "y":
                break
            else:
                value = roll_die()

            if value == 1:
                print("You rolled a 1! turn done")
                current_score = 0
                print("You rolled a", value, "your score is ", current_score)
                break

            else:
                current_score += value
                print("You rolled ", value, "your score is a", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is ", player_scores[player_idx])
