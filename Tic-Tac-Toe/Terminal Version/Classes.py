from Functions import *
from os import system
from random import randint

class Grid:

    def __init__(self):
        
        self.positions = [[" " for x in range(3)] for y in range(3)]
        self.colored_positions = [[" " for x in range(3)] for y in range(3)]

    def showGrid(self):
        
        print()
        
        for x in range(3):
            
            print("   |   |    ||")
            
            for y in range(3):
                
                print(" {} ".format(self.colored_positions[x][y]), end = "")
                print("|", end = "") if y != 2 else print(" || ", end = "")
                
            match x:
                
                case 0:
                    
                    print("The x axis is horizontal : [1,3]")
                    
                case 1:
                    
                    print("The y axis is vertical : [1,3]")
                    
                case 2:
                    
                    print(colored("Player: Blue Symbols", "blue"),"-",colored("Enemy: Red Symbols", "red"))
                
            print("___|___|___ ||") if x != 2 else print("   |   |    ||")
        
    def playerTurn(self, symbols):

        move = input("\nInput the coordinates (x,y) to make a move: ")

        try:
            
            move = move.split(",", 1)

            if not 1 <= int(move[0]) <= 3 or not 1 <= int(move[1]) <= 3:

                return errorMessage(self, symbols)
            
            y = int(move[0]) - 1
            x = abs(int(move[1]) - 3)

            if self.positions[x][y] != " ":

                return errorMessage(self, symbols)

            self.positions[x][y] = symbols[0]
            self.colored_positions[x][y] = colored(symbols[0], "blue")

        except (ValueError):

            return errorMessage(self, symbols)

    def enemyTurn(self, symbols):

        x = randint(0, 2)
        y = randint(0, 2)

        if self.positions[x][y] != " ":

            return self.enemyTurn(symbols)

        self.positions[x][y] = symbols[1]
        self.colored_positions[x][y] = colored(symbols[1], "red")
            
    def checkWinner(self, symbols):
        
        winner = ""
        
        for x in range(3):
            
            for y in range(3):
                
                winner += self.positions[x][y]
            
            output = self.checkWinnerAuxiliary(winner, symbols)
            
            if output != "Tie": return output
            
            winner = ""
            
        for y in range(3):
            
            for x in range(3):
                
                winner += self.positions[x][y]
                
            output = self.checkWinnerAuxiliary(winner, symbols)
            
            if output != "Tie": return output
            
            winner = ""
            
        for x, y in zip(range(3), range(3)):
            
            winner += self.positions[x][y]
            
        output = self.checkWinnerAuxiliary(winner, symbols)
        
        if output != "Tie": return output
        
        winner = ""
        
        for x, y, in zip(range(3), range(2, -1, -1)):
            
            winner += self.positions[x][y]
        
        return self.checkWinnerAuxiliary(winner, symbols)

    def checkWinnerAuxiliary(self, input, symbols):
        
        if input == "XXX":
                    
            return "Player" if symbols[0] == "X" else "Enemy"
        
        if input == "OOO":
                    
            return "Player" if symbols[0] == "O" else "Enemy"
        
        return "Tie"    