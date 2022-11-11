from Classes import *
from os import system
from termcolor import colored

def displayTitle():
    
    print(colored("= Tic-Tac-Toe ==========================================", attrs = ["bold"]))

def getSymbols():

    player_symbol = input("\nWhich symbol do you want to be? X or O? (X/O)? ")

    if player_symbol != "X" and player_symbol != "O":

        system('cls')
        displayTitle()
        print("\nInvalid symbol. Please try again.")
        return getSymbols()

    enemy_symbol = "X" if player_symbol == "O" else "O"
    return [player_symbol, enemy_symbol]

def errorMessage(grid, symbols):
    
    system('cls')
    displayTitle()
    grid.showGrid()
    print("\nInvalid coordinates. Please try again.")
    return grid.playerTurn(symbols)
    
def playAgain(grid, text):
    
    play_again = input("\nDo you want to play again? Yes or no? (Y/N): ")
    
    if play_again != "Y" and play_again != "N":
        
        system('cls')
        displayTitle()
        grid.showGrid()
        print(text + "\n\nInvalid reply. Please try again.")
        return playAgain(grid, text)
    
    return False if play_again == "Y" else True