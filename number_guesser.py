import random

range_setter = input("What range of numbers do you want? ")

if range_setter.isdigit():
    range_setter = int(range_setter)

    if range_setter <= 0:
        print("Choose a number that is above 0")
        quit()
else:
    print("Please choose a number next time ")
    quit()

random_number = random.randint(1,range_setter)

guesses = 0
while True:
    guesses += 1
    guess = input("Guess a number: ")

    if guess.isdigit():
        guess = int(guess)

        if guess > range_setter:
            print("You guessed above your range")
            continue

        if guess == random_number:
            print("You got it!")
            break
        else:
            print("Unlucky! Try again")

        if guess > random_number:
            print("Too high this time")

        elif guess < random_number:
            print("Too low this time")

    else:
        print("Please choose a number next time ")
        continue

print("You got it in", guesses, "guesses")
