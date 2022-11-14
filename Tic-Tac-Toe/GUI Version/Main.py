from tkinter import *
from random import randint

class GUI:
    
    def __init__(self):
        
        self.window = Tk()
        self.window.configure(bg = "black")
        icon = PhotoImage(file = "Icon.png")
        self.window.iconphoto(False, icon)
        self.window.title("Tic-Tac-Toe Game")
        self.window.geometry("300x350")
        
        self.top_frame = Frame(self.window, bg = "black")
        self.top_labelA = Label(self.top_frame, text = "Choose your symbol: ", background = "black", fg = "white", font = "bold")
        self.top_labelB = Label(self.top_frame, bg = "black")
        self.top_labelC = Label(self.top_frame, bg = "black", font = "bold")
        self.button_X = Button(self.top_frame, text = "X", bg = "black", font = "bold", fg = "white", borderwidth = 0, command = lambda : self.startGame("X"))
        self.button_O = Button(self.top_frame, text = "O", bg = "black", font = "bold", fg = "white", borderwidth = 0, command = lambda : self.startGame("O"))
        self.top_labelA.pack(side = LEFT)
        self.button_X.pack(side = LEFT)
        self.button_O.pack(side = LEFT)
        self.top_frame.pack()
        
        self.middle_frame = Frame(self.window)
        self.positions = [[" " for row in range(3)] for column in range(3)]
        self.symbols = [None, None]
        self.turns = 0
        
        for row in range(3):
            
            for column in range(3):
                
                self.positions[row][column] = Button(self.middle_frame,
                                                     state = "disabled",
                                                     text = self.positions[row][column],
                                                     bg = "white", fg = "black", font = "bold",
                                                     width = 10, height = 4,
                                                     command = lambda row = row, column = column : self.playerTurn(row, column))
                self.positions[row][column].grid(row = row, column = column)
                
        self.middle_frame.pack()
        
        self.bottom_frame = Frame(self.window, bg = "black")
        self.bottom_labelA = Label(self.bottom_frame, bg = "black", fg = "white")
        self.bottom_labelB = Label(self.bottom_frame, bg = "black", fg = "white")
        self.button_yes = Button(self.bottom_frame, text = "Yes", bg = "black", borderwidth = 0, fg = "white", command = lambda : self.restartGame())
        self.button_no = Button(self.bottom_frame, text = "No", bg = "black", borderwidth = 0, fg = "white", command = lambda : self.endMessage())
        
        self.bottom_labelB.config(text = "Do you want to play again?")
        self.bottom_labelA.pack(side = LEFT)
        self.bottom_labelB.pack(side = LEFT)
        self.button_yes.pack(side = LEFT)
        self.button_no.pack(side = LEFT)
        
        self.window.mainloop()
         
    def startGame(self, player_symbol):
        
        self.button_X.pack_forget()
        self.button_O.pack_forget()
        self.symbols = ["X", "O"] if player_symbol == "X" else ["O", "X"]
        self.top_labelA.config(text = "Player Symbol: {}".format(self.symbols[0]), fg = "#00FFFF")
        self.top_labelB.config(text = " | ", bg = "black", fg = "white")
        self.top_labelC.config(text = "Enemy Symbol: {}".format(self.symbols[1]), fg = "#FF6A6A")
        self.top_labelB.pack(side = LEFT)
        self.top_labelC.pack(side = LEFT)
        
        for row in range(3):
            
            for column in range(3):
                
                self.positions[row][column]["state"] = "normal"
        
        if player_symbol == "O":
            
            self.enemyTurn()
            
    def playerTurn(self, row, column):
        
        self.positions[row][column]["text"] = self.symbols[0]
        self.positions[row][column]["bg"] = "#00FFFF"
        self.positions[row][column]["state"] = "disabled"
        self.turns += 1
        
        value = self.checkEnd()
        
        self.enemyTurn() if self.turns != 9 and value[0] is False else self.endGame(value[1])
        
    def enemyTurn(self):
        
        row = randint(0, 2)
        column = randint(0, 2)
        
        while self.positions[row][column]["state"] != "normal":
            
            row = randint(0, 2)
            column = randint(0, 2)
    
        self.positions[row][column]["text"] = self.symbols[1]
        self.positions[row][column]["bg"] = "#FF6A6A"
        self.positions[row][column]["state"] = "disabled"
        self.turns += 1
        
        value = self.checkEnd()
        
        if self.turns == 9 or value[0] is True:
            
            self.endGame(value[1]) 
        
    def checkEnd(self):
        
        for row in range(3):
                
            if self.positions[row][0]["text"] == self.positions[row][1]["text"] == self.positions[row][2]["text"] != " ":
                
                return (True, self.positions[row][0]["text"])
            
        for column in range(3):
                
            if self.positions[0][column]["text"] == self.positions[1][column]["text"] == self.positions[2][column]["text"] != " ":
                
                return (True, self.positions[0][column]["text"])
            
        if self.positions[0][0]["text"] == self.positions[1][1]["text"] == self.positions[2][2]["text"] != " ":
            
            return (True, self.positions[0][0]["text"])
        
        if self.positions[2][0]["text"] == self.positions[1][1]["text"] == self.positions[0][2]["text"] != " ":
        
            return (True, self.positions[2][0]["text"])
        
        return (False, " ")
        
    def endGame(self, value):
        
        for row in range(3):
        
            for column in range(3):
                
                self.positions[row][column]["state"] = "disabled"
                
        match value:
            
            case " ":
                
                self.bottom_labelA.config(text = "It is a tie!", fg = "white")
                
            case "X":
                
                self.bottom_labelA.config(text = "You won!", fg = "#00FFFF") if self.symbols[0] == "X" else self.bottom_labelA.config(text = "You lost!", fg = "#FF6A6A")
                
            case "O":
                
                self.bottom_labelA.config(text = "You won!", fg = "#00FFFF") if self.symbols[0] == "O" else self.bottom_labelA.config(text = "You lost!", fg = "#FF6A6A")

        self.bottom_frame.pack()
        
    def endMessage(self):
        
        self.bottom_labelA.config(text = "Thank you for playing!", fg = "white")
        self.bottom_labelB.pack_forget()
        self.button_yes.pack_forget()
        self.button_no.pack_forget()
        
    def restartGame(self):
        
        self.bottom_frame.pack_forget()
        self.top_labelB.pack_forget()
        self.top_labelC.pack_forget()
        self.top_labelA.config(text = "Choose your symbol", fg = "white")
        self.button_X.pack(side = LEFT)
        self.button_O.pack(side = LEFT)
        self.turns = 0
        
        for row in range(3):
            
            for column in range(3):
                
                self.positions[row][column]["state"] = "disabled"
                self.positions[row][column]["text"] = " "
                self.positions[row][column]["bg"] = "white"

window = GUI()