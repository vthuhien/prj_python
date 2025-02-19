import random

user_wins = 0
computer_wins = 0

option = ["rock", "paper", "scissor"]

while True:
    user_pick = input("Type Rock/ Paper/ Scissor or Q to quit: ").lower()
    if user_pick == "q":
        break
    
    if user_pick not in option:    #it will check the input result 
        continue  

    r = random.randint(0,2)
    computer_pick = option[r]
    # rock : 0, paper:1, scissors:2
    print("Computer picked", computer_pick)

    if user_pick == "rock" and computer_pick == "scissor":
        print(" You won")
        user_wins += 1
    elif user_pick == "paper" and computer_pick == "rock":
        print(" You won")
        user_wins += 1
    elif user_pick == "scissor" and computer_pick == "paper":
        print(" You won")
        user_wins += 1
    elif user_pick == computer_pick:
        print("It's a tie")
    else:
        print("You lost")
        computer_wins += 1

print("You win", user_wins, "times")
print("Computer wins", computer_wins, "times")
