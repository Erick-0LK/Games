from Classes import *
from Functions import *
from termcolor import colored
from os import system

end_applicationn = False

while end_applicationn is False:

    move = [1, 1]
    map = Map()
    
    while map.tries != 0 and map.enemies != 0:

        system('cls')
        displayTitle()
        map.showMap()
        move = map.playerMove(move)
        
    system('cls')
    displayTitle()
    map.showMap()
    
    if map.enemies == 0:
        
        text = colored("Congratulations! You won.", "green")
        print(text)
        
    else:
        
        text = colored("You lost! Better luck next time.", "red")
        print(text)
        
    end_applicationn = playAgain(text, map)
    
system('cls')
print("The application has ended. Thanks for playing.")