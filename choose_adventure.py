print("Welcome to the Choose Your Own Adventure Game!")
name = input("What is your name? ")
print("Hello, " + name + "! Let's start the adventure.")

input1 = input("You found yourself in a wide road. Do you walk at the center or use the sidewalk? (center/sidewalk) ").lower()

if input1 == "center":
    print("You walk at the center of the road and suddenly a car comes speeding towards you. You got hit and lost the game.")
    
elif input1 == "sidewalk":
    input2 = input("You saw a beautiful gate written University of Eldoret. Do you enter or keep walking? (enter/walk) ").lower()
    
    if input2 == "enter":
        input3 = input("You entered the school and found a library. Do you go to the library or explore the campus? (library/explore) ").lower()
        
        if input3 == "library":
          print("You entered the library and found a snake at the entrance! You got bitten and lost the game.")
          
        elif input3 == "explore":
          input4 = input("You went to the field and found multiple games which one would you like to join? (football/basketball/tennis/hockey) ").lower()
          
          if input4 == "football":
            print("There are very many players in the football game and you could not get a chance. you Lost!")
            
          elif input4 == "basketball":
            print("You are too short for basketball. You lost!")
            
          elif input4 == "tennis":
            print("You are not good at tennis. You lost!")
            
          elif input4 == "hockey":
            input5 = input("You joined hockey and found a friendly Team Manager. Would you like to befriend him? (yes/no) ").lower()
            
            if input5 == "yes":
              print("The team manager destroys your mood and made you quit the game. You lost!")
              
            elif input5 == "no":
              print("You ignored the team manager and kept playing. You won the game!")
              
            else:
              print("Invalid input.You lost the game.")
                  
          else:
            print("Invalid input.You lost the game.")    
        
    elif input2 == "walk":
        input3 = input("You kept walking and found a man called Kibet. Do you talk to him or ignore him? (talk/ignore) ").lower()
        
        if input3 == "talk":
          print("Kibet did not like you because you are not a Kalenjin. He bit you on the neck and died. You lost the game.")
          
        elif input3 == "ignore":
          print("You ignored Kibet and kept walking. He got angry and started chasing you and you could not escape. You lost the game!")  
        
        else:
          print("Invalid input.You lost the game.")
    else:
        print("Invalid input.You lost the game.")
else:
    print("Invalid input.You lost the game.")
    
print("Thank you for playing the game, " + name + "!")