import turtle
import random
import time

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "blue", "green", "yellow", "orange",
          "purple", "pink", "brown", "gray", "cyan"]


def get_data():
    data = 0
    while True:
        data = input("How many turtles would you like to race(2-10) ? ")
        if data.isdigit():
            data = int(data)
        else:
            print("Please enter a valid number.")
            continue

        if data > 1 and data < 11:
            return data
        else:
            print("Please enter a number between 2 and 10.")


def race_turtles(colors):
    turtles = create_racer(colors)
    while True:
        for racer in turtles:
            distance = random.randint(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 20:
                return colors[turtles.index(racer)]


def create_racer(color):
    turtles = []
    spacingt = WIDTH // (len(color) + 1)
    for i, color in enumerate(color):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.color(color)
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingt, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles


def create_turtles():
    screen = turtle.Screen()
    screen.title("Turtle Race")
    screen.setup(WIDTH, HEIGHT)
    # time.sleep(6)


def draw_finish_line():
    line = turtle.Turtle()
    line.hideturtle()
    line.penup()
    line.speed(0)
    line.setpos(-WIDTH // 2, HEIGHT // 2 - 20)
    line.pendown()
    line.setpos(WIDTH // 2, HEIGHT // 2 - 20)


racers = get_data()
data = create_turtles()
draw_finish_line()
colors = random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race_turtles(colors)
time.sleep(5)
# print(colors)
print(f"The {winner} turtle wins!")
