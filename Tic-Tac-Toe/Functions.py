from Classes import *
import os, random

def displayTitle():
    
    print("= Tic-Tac-Toe ==================================")

def getSymbols():

    player_symbol = input("\nWhich symbol do you want to be? X or O? (X/O)? ")

    if player_symbol != "X" and player_symbol != "O":

        os.system('cls')
        displayTitle()
        print("\nInvalid symbol. Please try again.")

        return getSymbols()

    enemy_symbol = "X" if player_symbol == "O" else "O"
        
    return [player_symbol, enemy_symbol]

def playerTurn(symbols, grid):

    move = input("\nInput the coordinates (x,y) to make a move: ")

    try:

        if len(move) != 3 or move[1] != ",":

            os.system('cls')
            displayTitle()
            grid.showGrid()
            print("\nInvalid coordinates. Please try again.")

            return playerTurn(symbols, grid)

        move = move.split(",")
        x = int(move[0]) - 1
        y = int(move[1]) - 1

        if grid.positions[x][y] != " ":

            os.system('cls')
            displayTitle()
            grid.showGrid()
            print("\nInvalid coordinates. Please try again.")

            return playerTurn(symbols, grid)

        grid.positions[x][y] = symbols[0]

    except (IndexError, ValueError):

        os.system('cls')
        displayTitle()
        grid.showGrid()
        print("\nInvalid coordinates. Please try again.")

        return playerTurn(symbols, grid)

def enemyTurn(symbols, grid):

    x = random.randint(0, 2)
    y = random.randint(0, 2)

    if grid.positions[x][y] != " ":

        return enemyTurn(symbols, grid)

    grid.positions[x][y] = symbols[1]
    
def playAgain(text, grid):
    
    play_again = input("\nDo you want to play again? Yes or no? (Y/N): ")
    
    if play_again != "Y" and play_again != "N":
        
        os.system('cls')
        displayTitle()
        grid.showGrid()
        print(text + "\n\nInvalid reply. Please try again.")
        
        return playAgain(text, grid)
    
    return False if play_again == "Y" else True