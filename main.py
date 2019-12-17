import os
from characters.character import Person
from game.factory import Start
# from characters.magicien import Magicien
from characters.orc import Orc
from characters.loup import Loup
from characters.zombie import Zombie

if __name__=='__main__':

    Start.enter_name()
    Start.choice_hero()

    # character.enter_name()

   # gue = Guerrier("nicos")
    #print(gue.__dict__)
    # mag = Magicien("nicos")
    # print(mag.__dict__)
    a= Orc()
    print (a.__dict__)
    b= Loup()
    print (b.__dict__)
    c= Zombie()
    print (c.__dict__)
    #narration
    #start game
    #random choice ennemiss
    #display game choice
    #choose choice attack or stop combat
    #program play
    #display result