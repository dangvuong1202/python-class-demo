from random import Ranint
print("Chon Dam, La, Keo: ")
player = input()
computer = Ranint(0,2)
if computer == 0:
    computer = "Dam"
if computer == 1:
    computer = "La"
if computer == 2:
    computer = "Keo"
print("---")
print("Your's Choose: "+player)
print("Computer's Choose: "+computer)
if player==computer:
    print("Draw")
else:
    if player == "Keo":
        if computer == "Dam":
            print("Lose")
        else:
            print("Win")
    if player == "La":
        if computer == "Dam":
            print("Win")
        else:
            print("Lose")
    if player == "Dam":
        if computer == "La":
            print("Lose")
        else:
            print("Win")
            
