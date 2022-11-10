from Functions import *
from os import system
from random import randint

class Grid():

    def __init__(self):
        
        self.positions = [[" " for x in range(3)] for y in range(3)]
        self.colored_positions = [[" " for x in range(3)] for y in range(3)]

    def showGrid(self):
                
        print()
        print("   |   |   ")
        print(" {} | {} | {}  \u2191".format(self.colored_positions[0][0], self.colored_positions[0][1], self.colored_positions[0][2]))
        print("___|___|___")
        print("   |   |   ")
        print(" {} | {} | {}  y".format(self.colored_positions[1][0], self.colored_positions[1][1], self.colored_positions[1][2]))
        print("___|___|___")
        print("   |   |    ")
        print(" {} | {} | {}  \u2191".format(self.colored_positions[2][0], self.colored_positions[2][1], self.colored_positions[2][2]))
        print("   |   |   ")
        print("\n \u2192   x   \u2192 ")
        
    def playerTurn(self, symbols):

        move = input("\nInput the coordinates (x,y) to make a move: ")

        try:

            if len(move) != 3 or move[1] != "," or move[0] == "0" or move[2] == "0":

                system('cls')
                displayTitle()
                self.showGrid()
                print("\nInvalid coordinates. Please try again.")

                return self.playerTurn(symbols)

            move = move.split(",")
            y = int(move[0]) - 1
            x = abs(int(move[1]) - 3)

            if self.positions[x][y] != " ":

                system('cls')
                displayTitle()
                self.showGrid()
                print("\nInvalid coordinates. Please try again.")

                return self.playerTurn(symbols)

            self.positions[x][y] = symbols[0]
            self.colored_positions[x][y] = colored(symbols[0], "blue")

        except (IndexError, ValueError):

            system('cls')
            displayTitle()
            self.showGrid()
            print("\nInvalid coordinates. Please try again.")

            return self.playerTurn(symbols)

    def enemyTurn(self, symbols):

        x = randint(0, 2)
        y = randint(0, 2)

        if self.positions[x][y] != " ":

            return self.enemyTurn(symbols)

        self.positions[x][y] = symbols[1]
        self.colored_positions[x][y] = colored(symbols[1], "red")
            
    def checkWinner(self, symbols):
        
        winner = ""
        
        for x in range(0, 3):
            
            for y in range(0, 3):
                
                winner += self.positions[x][y]
            
            output = self.checkWinnerAuxiliary(winner, symbols)
            
            if output != "Tie": return output
            
            winner = ""
            
        for y in range(0, 3):
            
            for x in range(0, 3):
                
                winner += self.positions[x][y]
                
            output = self.checkWinnerAuxiliary(winner, symbols)
            
            if output != "Tie": return output
            
            winner = ""
            
        for x, y in zip(range(0, 3), range(0, 3)):
            
            winner += self.positions[x][y]
            
        output = self.checkWinnerAuxiliary(winner, symbols)
        
        if output != "Tie": return output
        
        winner = ""
        
        for x, y, in zip(range(0, 3), range(2, -1, -1)):
            
            winner += self.positions[x][y]
        
        return self.checkWinnerAuxiliary(winner, symbols)

    def checkWinnerAuxiliary(self, input, symbols):
        
        if input == "XXX":
                    
            return "Player" if symbols[0] == "X" else "Enemy"
        
        if input == "OOO":
                    
            return "Player" if symbols[0] == "O" else "Enemy"
        
        return "Tie"    