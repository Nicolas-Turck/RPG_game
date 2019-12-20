from .character import Person
import time
import os
class Guerrier(Person):
    """class for guerrier player"""
    def __init__(self, name):
        self.name = name
        super().__init__(500, 50, 80, 10, name)
        
    def heal(self, player):
        self.player = player
        print("vous n'etes pas magiciens!!")
        time.sleep(2)
        os.system('cls||clear')
