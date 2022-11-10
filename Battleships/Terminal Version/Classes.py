from Functions import *
from os import system
from random import randint

class Map():

    def __init__(self):

        self.positions = [[0 for x in range(5)] for y in range(5)]
        self.enemy_positions = [[0 for x in range(5)] for y in range(5)]
        self.tries = 10
        self.enemies = 5
        self.setEnemyPositions()

    def showMap(self):

        map = {0 : "X", 1 : "O", 2 : "*"}

        print("Number of enemies left: {}".format(self.enemies))
        print("Number of tries left: {}\n".format(self.tries))

        for x in range(5):

            for y in range(5):

                print(map[self.positions[x][y]] + " ", end = "")
                
                if y == 4:

                    print(" y") if x == 2 else print(" v")

        print("\n>>> x >>>\n")

    def setEnemyPositions(self):

        counter = 0

        while counter != 5:

            x = randint(0, 4)
            y = randint(0, 4)

            if self.enemy_positions[x][y] == 0:

                self.enemy_positions[x][y] = 1
                counter += 1

    def playerMove(self):

        move = input("Input the coordiantes in the format (x,y) to attack: ")

        try:

            if len(move) != 3 or move[0] == "0" or move[1] != "," or move[2] == "0":

                system('cls')
                displayTitle()
                self.showMap()
                print("Invalid coordinates. Please try again.\n")

                return self.playerMove()

            move = move.split(",")
            y = int(move[0]) - 1
            x = int(move[1]) - 1

            if self.positions[x][y] != 0:

                system('cls')
                displayTitle()
                self.showMap()
                print("Invalid coordinates. Please try again.\n")

                return self.playerMove()

            if self.enemy_positions[x][y] == 1:

                self.positions[x][y] = 1
                self.enemy_positions[x][y] = 0
                self.enemies -= 1

            elif self.enemy_positions != 1:

                self.positions[x][y] = 2

            self.tries -= 1

        except (IndexError, ValueError):

            system('cls')
            displayTitle()
            self.showMap()
            print("Invalid coordinates. Please try again.\n")

            return self.playerMove()

    def getClosestEnemies(x, y):

        closest = 5

        for i in range(5):

            for j in range(5):

                print(i)





