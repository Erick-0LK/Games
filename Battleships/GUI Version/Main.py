from tkinter import *
from random import randint

class GUI:
    
    def __init__(self):
        
        self.window = Tk()
        self.window.configure(bg = "blue")
        icon = PhotoImage(file = "Icon.png")
        self.window.iconphoto(False, icon)
        self.window.title("Battleships Game")
        self.window.geometry("600x320")
        
        self.top_frame = Frame(self.window)
        self.positions = [[None for i in range(10)] for j in range(5)]
        self.enemy_positions = [[0 for i in range(10)] for j in range(5)]
        self.enemies = 5
        self.tries = 15
        self.setEnemyPositions()
        
        for row in range(5):
            
            for column in range(10):
                
                self.positions[row][column] = Button(self.top_frame,
                                                     text = "?",
                                                     bg = "white", fg = "black", font = "bold",
                                                     width = 5, height = 2,
                                                     command = lambda row = row, column = column : self.playerMove(row, column))
                self.positions[row][column].grid(row = row, column = column)
        
        self.top_frame.pack()
        
        self.labelA = Label(relief = "solid", bg = "white", border = 2, fg = "black", font = "bold", text = "Number of tries left: {} | Number of enemies left: {}".format(self.tries, self.enemies))
        self.labelB = Label(relief = "solid", bg = "white", border = 2, fg = "black", font = "bold", text = "Click on a tile to make a move and receive a hint to the nearest enemy...")
        self.labelA.place(x = 25, y = 260)
        self.labelB.place(x = 25, y = 285)
        self.button_yes = Button(text = "Yes", bg = "white", bd = 1, font = "bold", fg = "black", command = lambda : self.restartGame())
        self.button_no = Button(text = "No", bg = "white", bd = 1, font = "bold", fg = "black", command = lambda : self.endMessage())
        
        self.window.bind("<KeyRelease>", self.revealEnemyPostions)
        self.window.mainloop()
        
    def setEnemyPositions(self):
        
        counter = 0

        while counter != 5:

            column = randint(0, 9)
            row = randint(0, 4)

            if self.enemy_positions[row][column] == 0:

                self.enemy_positions[row][column] = 1
                counter += 1
            
    def playerMove(self, row, column):
        
        self.positions[row][column]["state"] = "disabled"
        self.positions[row][column]["text"] = "\N{check mark}" if self.enemy_positions[row][column] == 1 else "X"
        
        if self.positions[row][column]["text"] == "\N{check mark}":
            
            self.positions[row][column]["bg"] = "#99FF75"
            self.enemy_positions[row][column] = 0
            self.enemies -= 1
            
        else:
            
            self.positions[row][column]["bg"] = "#FF5151"
            
        self.tries -=1
        self.labelA.config(text = "Number of tries left: {} | Number of enemies left: {}".format(self.tries, self.enemies))
        self.getClosestEnemy(row, column) if self.enemies != 0 and self.tries != 0 else self.endGame()
        
    def getClosestEnemy(self, x, y):

        closest = 100

        for row in range(5):

            for column in range(10):
                
                if self.enemy_positions[row][column] == 1 and abs(row - x) + abs(column - y) < closest:
                    
                    closest = abs(row - x) + abs(column - y)
                    
        if closest == 1:
            
            self.labelB.config(text = "The nearest enemy to position [{}][{}] is {} space away.".format(y + 1, abs(x - 5), closest))
                    
        else:
            
            self.labelB.config(text = "The nearest enemy to position [{}][{}] is {} spaces away.".format(y + 1, abs(x - 5), closest))
            
    def endGame(self):
        
        for row in range(5):

            for column in range(10):
                
                self.positions[row][column]["state"] = "disabled"
        
        if self.enemies == 0:
            
            self.labelB.config(text = "Congratulations! You won! Do you want to play again?")
            self.button_yes.place(x = 410, y = 282)
            self.button_no.place(x = 450, y = 282)
            
        else:
            
            self.labelB.config(text = "You lost! Better luck next time! Do you want to play again?")
            self.button_yes.place(x = 440, y = 282)
            self.button_no.place(x = 480, y = 282)       
            
    def revealEnemyPostions(self, event):
        
        if event.keysym == "s":
        
            for row in range(5):

                for column in range(10):
                    
                    if self.enemy_positions[row][column] == 1:
                        
                        self.positions[row][column]["bg"] = "yellow"
                        
    def restartGame(self):
        
        self.button_yes.place_forget()
        self.button_no.place_forget()
        
        for row in range(5):

            for column in range(10):
                
                self.positions[row][column]["state"] = "normal"
                self.positions[row][column]["text"] = "?"
                self.positions[row][column]["bg"] = "white"
                self.enemy_positions[row][column] = 0
                
        self.setEnemyPositions()
        self.tries = 15
        self.enemies = 5
        self.labelA.config(text = "Number of tries left: {} | Number of enemies left: {}".format(self.tries, self.enemies))
        self.labelB.config(text = "Click on a tile to make a move and receive a hint to the nearest enemy...")
        
    def endMessage(self):
        
        self.button_yes.place_forget()
        self.button_no.place_forget()
        self.labelB.place_forget()
        self.labelA.config(text = "Thanks for playing!")
        
window = GUI()