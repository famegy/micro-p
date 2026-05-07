import random
import time

OPERATORS = ['+', '-', '*', ]
TOTALPROBLEMS = 10
min_value = 4
max_value = 20


def generate_problem():
    num1 = random.randint(min_value, max_value)
    num2 = random.randint(min_value, max_value)
    operator = random.choice(OPERATORS)
    expr = str(num1) + " " + operator + " " + str(num2)
    answer = eval(expr)
    return expr, answer


wrong = 0

starting_time = time.time()

print("..................................")

for i in range(TOTALPROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem # " + str(i+1) + ": " + expr + " = ")
        if guess == str(answer):
            break
            break

        wrong += 1


end_time = time.time()

time_spent = round(end_time - starting_time, 2)
print("Time spent: " + str(time_spent) + " seconds")
print("Wrong answers: " + str(wrong))
print("..................................")
