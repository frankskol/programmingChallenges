import random

def RockPaperScissors (choice):
    computerchoice = random.randint(0, 2)
    if choice == 0:
        if computerchoice == 0:
            print ("Computer chose rock! It's a tie!")
        elif computerchoice == 1:
            print ("Computer chose scissors! You win!")
        elif computerchoice == 2:
            print ("Computer chose paper! You lose!")
    elif choice == 1:
        if computerchoice == 0:
            print ("Computer chose rock! You lose!")
        elif computerchoice == 1:
            print ("Computer chose scissors! It's a tie!")
        elif computerchoice == 2:
            print ("Computer chose paper! You win!")
    elif choice == 2:
        if computerchoice == 0:
            print ("Computer chose rock! You win!")
        elif computerchoice == 1:
            print ("Computer chose scissors! You lose!")
        elif computerchoice == 2:
            print ("Computer chose paper! It's a tie!")
    

while True:
    Chosen = False
    while Chosen == False:
        Userchoice = str(input("Rock, Paper, Scissors! Make your choice:\n"))
        if Userchoice == ("rock" or "Rock"):
            RockPaperScissors(0)
            Chosen = True
        elif Userchoice == ("scissors" or "Scissors"):
            RockPaperScissors(1)
            Chosen = True
        elif Userchoice == ("paper" or "Paper"):
            RockPaperScissors(2)
            Chosen = True
        else:
            print ("No input! Try again")
   