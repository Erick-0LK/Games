from Classes import *
from termcolor import colored
from os import system

def displayTitle():

    print(colored("= Battleships ===============================================================================\n", attrs = ["bold"]))
    
def errorMessage(map, previous_move):
    
    system('cls')
    displayTitle()
    map.showMap()
    print("Invalid coordinates. Please try again.\n")
    return map.playerMove(previous_move)

def playAgain(map, text):
    
    play_again = input("\nDo you want to play again? Yes or no? (Y/N): ")
    
    if play_again != "Y" and play_again != "N":
        
        system('cls')
        displayTitle()
        map.showMap()
        print(text + "\n\nInvalid reply. Please try again.")
        
        return playAgain(map, text)
    
    return False if play_again == "Y" else True