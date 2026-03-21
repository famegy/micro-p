print("Welcome to Quizzes")
name = input("What is your name? ")
print("welcome " + str(name))
start = input("Would you like to start a quiz? (y/n) ").lower()

score = 0

if start.lower() != 'y':
    quit()

print("let's play:)")

answer = input("What is RAM in full? ")

if answer.lower() == "random access memory":
    print("correct")
    score += 1
else:
    print("incorrect")


answer = input("What is CPU in full? ")

if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")


answer = input("What is the first phase of compilation? ")

if answer.lower() == "lexical analysis":
    print("correct")
    score += 1
else:
    print("incorrect")


answer = input("What is ROM in full? ")

if answer.lower() == "read only memory":
    print("correct")
    score += 1
else:
    print("incorrect")



answer = input("What is GPU in full? ")

if answer.lower() == "graphics processing unit":
    print("correct")
    score += 1
else:
    print("incorrect")

print("you got " + str(score) + " points out of 5" )
print("you scored " + str((score/5)*100) + "%")