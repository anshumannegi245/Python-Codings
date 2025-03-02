import random


player_score = 0
computer_score =0


def computers():
    computer_choose = random.randint(1,3)
    if computer_choose == 1:
        choice = "r"
    elif computer_choose == 2:
        choice = "s"
    elif computer_choose == 3:
        choice = "p"
    return choice

def players():
    players_choose = input("Enter Rock , Scissors , Paper ")
    if players_choose in ["Rock","R","r","rock"]:
        p_choice = "r"
    elif players_choose in ["Paper","paper","p","P"]:
        p_choice = "p"
    elif players_choose in ["Scissors","scissors","s","S"]:
        p_choice = "s"    
    return p_choice

user = players()
computer = computers()

while True:
    if user == "r":
        if computer == "r":
            print("The value is Same as rock")
            print("")
        elif computer == "p":
            print("")
            print("You lose ")
            computer_score +=1
        elif computer == "s":
            print("")
            print("You won")
            player_score +=1
    elif user == "p":
        if computer == "r":
            print("you Won")
            print("")
            player_score +=1
        elif computer == "p":
            print("")
            print(" The value is Same as Paper")
#             computer_score +=1  I have done wrong in the video please remove this line
        elif computer == "s":
            print("")
            print("You lose")
            computer_score +=1
            
    elif user == "s":
        if computer == "r":
            print("You lose")
            print("")
            computer_score += 1
        elif computer == "p":
            print("")
            print("You won ")
            player_score +=1
        elif computer == "s":
            print("")
            print("The value is Same as rock")
        
    print("The player score :"+str(player_score))
    print("The computer score :"+str(computer_score))
    life=input("Wanna continue(Y/N)")
    if life in ["Y","y"]:
        continue
    else:
        break

print("-----------------------------------------")
print("The game is Over")
