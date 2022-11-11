from Classes import *
from Functions import *
from termcolor import colored
from os import system

system('cls')
end_application = False

while end_application is False:

    turns = 0
    displayTitle()
    symbols = getSymbols()
    grid = Grid()
    system('cls')

    while True:

        displayTitle()

        if symbols[0] == "X":

            grid.showGrid()
            grid.playerTurn(symbols)

            if turns == 4 or grid.checkWinner(symbols) != "Tie":
                
                break

            grid.enemyTurn(symbols)
            
            if grid.checkWinner(symbols) != "Tie":
                
                break
            
            turns += 1
            system('cls')

        else:

            grid.enemyTurn(symbols)
            grid.showGrid()
            
            if turns == 4 or grid.checkWinner(symbols) != "Tie":
                
                break

            grid.playerTurn(symbols)
            
            if grid.checkWinner(symbols) != "Tie":
                
                break

            turns += 1
            system('cls')
            
    system('cls')
    displayTitle()
    grid.showGrid()
    winner = grid.checkWinner(symbols)
    
    if winner == "Player":
        
        text = colored("\nCongratulations! You won.", "blue")
        print(text)
            
    elif winner == "Enemy":
            
        text = colored("\nYou lost! Better luck next time.", "red")
        print(text)
            
    else:
        
        text = "\nIt is a tie!"
        print(text)
        
    end_application = playAgain(grid, text)
    system('cls')
    
print("The application has ended. Thanks for playing!")