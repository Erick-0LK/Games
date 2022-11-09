from Classes import *
from Functions import *
import os

os.system('cls')
end_application = False

while end_application is False:

    turns = 0
    displayTitle()
    symbols = getSymbols()
    grid = Grid()
    os.system('cls')

    while True:

        displayTitle()

        if symbols[0] == "X":

            grid.showGrid()
            playerTurn(symbols, grid)

            if turns == 4 or grid.checkWinner(symbols) != "Tie": break

            enemyTurn(symbols, grid)
            
            if grid.checkWinner(symbols) != "Tie": break
            
            turns += 1
            os.system('cls')

        else:

            enemyTurn(symbols, grid)
            grid.showGrid()
            
            if turns == 4 or grid.checkWinner(symbols) != "Tie": break

            playerTurn(symbols, grid)
            
            if grid.checkWinner(symbols) != "Tie": break

            turns += 1
            os.system('cls')
            
    os.system('cls')
    displayTitle()
    grid.showGrid()
    winner = grid.checkWinner(symbols)
    
    if winner == "Player":
        
        text = "\nCongratulations! You won."
        print(text)
            
    elif winner == "Enemy":
            
        text = "\nYou lost! Better luck next time."
        print(text)
            
    else:
        
        text = "\nIt is a tie!"
        print(text)
        
    end_application = playAgain(text, grid)
    os.system('cls')
    
print("The application has ended. Thanks for playing!")