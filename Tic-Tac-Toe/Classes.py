class Grid():

    def __init__(self):
        
        self.positions = [[" " for x in range(3)] for y in range(3)]

    def showGrid(self):

        print("\n   |   |   ")
        print(" {} | {} | {} ".format(self.positions[0][0], self.positions[0][1], self.positions[0][2]))
        print("___|___|___")
        print("   |   |   ")
        print(" {} | {} | {} ".format(self.positions[1][0], self.positions[1][1], self.positions[1][2]))
        print("___|___|___")
        print("   |   |   ")
        print(" {} | {} | {} ".format(self.positions[2][0], self.positions[2][1], self.positions[2][2]))
        print("   |   |   ")
        
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