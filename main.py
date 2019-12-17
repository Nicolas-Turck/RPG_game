import os
from characters.character import Person
from characters.magicien import Magicien
from characters.archer import Archer
from characters.guerrier import Guerrier
if __name__=='__main__':



    names = enter_name()

    mag = Magicien("nicos")
    arc = Archer("farid")
    print(mag.__dict__)
    print(arc.__dict__)
    #narration
    #start game
    #random choice ennemiss
    #display game choice
    #choose choice attack or stop combat
    #program play
    #display result