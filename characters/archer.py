from .character import Person
import os
import time
class Archer(Person):
    """class for archer player"""
    def __init__(self, name):
        self.name = name
        super().__init__(350, 80, 30, 50, name)

    def heal(self, player):
        self.player = player
        print("vous n'etes pas magiciens!!")
        time.sleep(2)
        os.system('cls||clear')

