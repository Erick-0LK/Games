from Functions import *
from termcolor import colored
from os import system
from random import randint

class Map:

    def __init__(self):

        self.x = 5
        self.y = 10
        self.tries = 15
        self.enemies = 5
        self.positions = [[0 for x in range(self.y)] for y in range(self.x)]
        self.enemy_positions = [[0 for x in range(self.y)] for y in range(self.x)]
        self.map = {0 : "X", 1 : colored("O", "green"), 2 : colored("*", "red"), 3 : colored("X", "yellow")}
        self.setEnemyPositions()

    def showMap(self):

        print("Number of enemies left: {}".format(self.enemies))
        print("Number of tries left: {}\n".format(self.tries))
        
        for x in range(self.x):
            
            print("   |   |   |   |   |   |   |   |   |    ||")
            
            for y in range(self.y):
                
                print(" {} ".format(self.map[self.positions[x][y]]), end = "")                         
                print("|", end = "") if y != self.y - 1 else print(" || ", end = "")
                
            match x:
                
                case 0:
                    
                    print("The x axis is horizontal : [1,10]")
                    
                case 1:
                    
                    print("The y axis is vertical : [1,5]")
                
                case 2:
                    
                    print("X : Unused coordinates.")
                    
                case 3:
                    
                    print(colored("O", "green"), ": Used coordinates which held an enemy.")
                    
                case 4:
                    
                    print(colored("*", "red"), ": Used coordinates which did not hold an enemy.")
                
            print("___|___|___|___|___|___|___|___|___|___ ||") if x != self.x - 1 else print("   |   |   |   |   |   |   |   |   |    ||\n")

    def setEnemyPositions(self):

        counter = 0

        while counter != 5:

            x = randint(0, self.x - 1)
            y = randint(0, self.y - 1)

            if self.enemy_positions[x][y] == 0:

                self.enemy_positions[x][y] = 1
                counter += 1

    def playerMove(self, previous_move):
        
        if previous_move is not False:
        
            x = abs(int(previous_move[1]) - self.x)
            y = int(previous_move[0]) - 1
            self.getClosestEnemy(x, y, previous_move)
            
        new_move = input("Input the coordiantes in the format (x,y) to attack: ")
        
        if new_move == "Cheat":
            
            self.revealEnemyPostions()
            return previous_move
        
        try:
        
            new_move = new_move.split(",", 1)
        
            if not 1 <= int(new_move[0]) <= self.y or not 1 <= int(new_move[1]) <= self.x:

                return errorMessage(self, previous_move)

            x = abs(int(new_move[1]) - self.x)
            y = int(new_move[0]) - 1
            
            if self.positions[x][y] == 1 or self.positions[x][y] == 2:

                return errorMessage(self, previous_move)
            
            if self.enemy_positions[x][y] == 1:

                self.positions[x][y] = 1
                self.enemy_positions[x][y] = 0
                self.enemies -= 1

            elif self.enemy_positions != 1:

                self.positions[x][y] = 2
                
            self.tries -= 1    
            self.getClosestEnemy(x, y, new_move)
            return new_move

        except (ValueError):

            return errorMessage(self, previous_move)

    def getClosestEnemy(self, x, y, move):

        closest = 5

        for i in range(self.x):

            for j in range(self.y):
                
                if self.enemy_positions[i][j] == 1 and abs(i - x) + abs(j - y) < closest:
                    
                    closest = abs(i - x) + abs(j - y)
                    
        if closest == 1:
            
            print("The nearest enemy to position [{}][{}] is {} space away.\n".format(move[0], move[1], closest))
                    
        else:
            
            print("The nearest enemy to position [{}][{}] is {} spaces away.\n".format(move[0], move[1], closest))
            
    def revealEnemyPostions(self):
        
        for i in range(self.x):

            for j in range(self.y):
                
                if self.enemy_positions[i][j] == 1:
                    
                    self.positions[i][j] = 3