#ROCK , PAPER , SCISSORS GAME IMPLEMENTATION 
again = 'y'
from random import randrange


def game(userChoice, computerChoice):
    
    if userChoice == computerChoice:
        print("Result : This is a Draw Match")

    #When User option is Rock
    if userChoice == 'Rock' and computerChoice == 'Scissors':
        print("Result : User wins")
    elif userChoice == 'Rock' and computerChoice == 'Paper': 
        print("Result : Computer wins")
 
        
    #When User option is Paper
    if userChoice == 'Paper' and computerChoice == 'Rock':
        print("Result : User wins")
    elif userChoice == 'Paper' and computerChoice == 'Scissors':
        print("Result : Computer wins")
        
    #When User option is Scissor
    if userChoice == 'Scissors' and computerChoice == 'Paper':
        print("Result : User wins")
    elif userChoice == 'Scissors' and computerChoice == 'Rock':
        print("Result : Computer wins")
       
def userInput():
    
    userChoice = input("What do you choose? Rock? Paper or Scissors? --> ")
    if userChoice == "Rock" or "Paper" or "Scissors":
        l = ['Rock','Paper','Scissors']
        cChoice = randrange(0,len(l))
        computerChoice = l[cChoice]
        print("Computer chooses : ",computerChoice)
        game(userChoice, computerChoice)
    
    #if userChoice != "Rock" or "Paper" or "Scissors":
    #    print("ENTER VALID USER INPUT")
   
while again == 'y':
    print("")
    userInput()
    again=input("Run again? Y or N?    ")
    
    if again != 'y':
        print("Goodbye")
        break 
        
