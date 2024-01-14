import random

name = input("enter your name: ")
user_option = input("enter the choices(Rock, Paper, Scissors ?) ")
possible_choices = ["Rock","Paper","Scissors"]
computer_option = random.choice(possible_choices)
print(f" you choose {user_option} and computer choose {computer_option}")

if user_option == computer_option:
  print("Both players selected",user_option,"It's a tie!",name)
  
elif user_option == "Rock":
  if computer_option == "Scissors":
    print("you win",name)
  else:
    print("you lose",name)

elif user_option =="Paper":
  if computer_option == "Rock":
    print("you win",name)
  else:
    print("you lose",name)

elif user_option == "scissors":
  if computer_option == "Paper":
    print("you win",name)
  else:
    print("you lose",name)
    
else:
  print("invalid input")