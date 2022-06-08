from ast import Break
import random
from re import U


while True:
 choices = ["r", "p", "s"]
 computer = random.choice(choices)
 player = None

 player =  input("pick an option from r, p, s: ").lower()
 while player not in choices:
       player = input("error...pick an option from r, p, s: ").lower()
 

 if player == computer:
    print("computer: ",computer)
    print("player: ",player)
    print("It's a tie")
    
    

 elif player == "r":
    if computer == "p":
       print("computer: ", computer)
       print("player: ", player)
       print("You Lose")
    if computer == "s":
       print("computer: ", computer)
       print("player: ", player)
       print("You Win")
    
    break
 

    

 elif player == "s":
    if computer == "r":
       print("computer: ", computer)
       print("player: ", player)
       print("You Lose")
    if computer == "p":
       print("computer: ", computer)
       print("player: ", player)
       print("You Win")

    break

 elif player == "p":
    if computer == "s":
       print("computer: ", computer)
       print("player: ", player)
       print("You Lose")
    if computer == "r":
       print("computer: ", computer)
       print("player: ", player)
       print("You Win")
    

    break
 
    
             


        


        
