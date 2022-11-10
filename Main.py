import sys
from Classes import *
from Functions import *
from os import system

end_applicationn = False

while end_applicationn is False:

    map = Map()

    while map.tries != 0 and map.enemies != 0:

        system('cls')
        displayTitle()
        map.showMap()
        map.playerMove()

    break