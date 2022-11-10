from Functions import *
from termcolor import colored
from os import system
from random import randint

class Map():

    def __init__(self):

        self.positions = [[0 for x in range(5)] for y in range(5)]
        self.enemy_positions = [[0 for x in range(5)] for y in range(5)]
        self.tries = 10
        self.enemies = 5
        self.cheat = False
        self.setEnemyPositions()

    def showMap(self):

        map = {0 : "X", 1 : colored("O", "green"), 2 : colored("*", "red")}

        print("Number of enemies left: {}".format(self.enemies))
        print("Number of tries left: {}\n".format(self.tries))

        for x in range(5):
            
            if x != 4:
            
                print("\u2191", end = " ")
                
            else:
                
                print("y", end = " ")

            for y in range(5):

                print(map[self.positions[x][y]] + " ", end = "")
                
                
            match x:
                
                case 0:
                    
                    print()
                
                case 1:
                    
                    print(" | X : Unused coordinates.")
                    
                case 2:
                    
                    print(" |", colored("O", "green"), ": Used coordinates which held an enemy.")
                    
                case 3:
                    
                    print(" |", colored("*", "red"), ": Used coordinates which did not hold an enemy.")
                        
        print("\n>>> x >>>\n")

    def setEnemyPositions(self):

        counter = 0

        while counter != 5:

            x = randint(0, 4)
            y = randint(0, 4)

            if self.enemy_positions[x][y] == 0:

                self.enemy_positions[x][y] = 1
                counter += 1

    def playerMove(self, previous_move):
        
        x = abs(int(previous_move[1]) - 5)
        y = int(previous_move[0]) - 1
        self.getClosestEnemy(x, y, previous_move)
        new_move = input("Input the coordiantes in the format (x,y) to attack: ")
        
        if new_move == "Cheat":
            
            self.showEnemyPositions()
            
            return self.playerMove(previous_move)
            
        try:

            if len(new_move) != 3 or not (1 <= int(new_move[0]) <= 5) or new_move[1] != "," or not (1 <= int(new_move[2]) <= 5):

                system('cls')
                displayTitle()
                self.showMap()
                print("Invalid coordinates. Please try again.\n")

                return self.playerMove(previous_move)

            new_move = new_move.split(",")
            x = abs(int(new_move[1]) - 5)
            y = int(new_move[0]) - 1

            if self.positions[x][y] != 0:

                system('cls')
                displayTitle()
                self.showMap()
                print("Invalid coordinates. Please try again.\n")

                return self.playerMove(previous_move)

            if self.enemy_positions[x][y] == 1:

                self.positions[x][y] = 1
                self.enemy_positions[x][y] = 0
                self.enemies -= 1

            elif self.enemy_positions != 1:

                self.positions[x][y] = 2

            self.tries -= 1
            self.getClosestEnemy(x, y, new_move)
            
            return new_move

        except (IndexError, ValueError):

            system('cls')
            displayTitle()
            self.showMap()
            print("Invalid coordinates. Please try again.\n")

            return self.playerMove(previous_move)

    def getClosestEnemy(self, x, y, move):

        closest = 5

        for i in range(5):

            for j in range(5):
                
                if self.enemy_positions[i][j] == 1 and abs(i - x) + abs(j - y) < closest:
                    
                    closest = abs(i - x) + abs(j - y)
                    
        if closest == 1:
            
            print("The nearest enemy is within {} space of position [{}][{}]\n".format(closest, move[0], move[1]))
                    
        else:
            
            print("The nearest enemy is within {} spaces of position [{}][{}]\n".format(closest, move[0], move[1]))
    
    def showEnemyPositions(self):
        
        print("\nThe remaining enemy postions are:\n")
        
        for x in range(5):
            
            for y in range(5):
                
                if self.enemy_positions[x][y] == 1:
                    
                    print("[{}][{}]".format(x + 1, y + 1), end = " ")
                    
        print("\n")