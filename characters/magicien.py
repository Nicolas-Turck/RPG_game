from .character import Person
import os
import time
class Magicien(Person):
    """class for create magicien player
    and use mana to heal"""
    def __init__(self, name):
        self.name = name
        self.mana = 50
        super().__init__(600, 20, 50, 25, name)


    def heal(self, player):
        """metho for healt and add 50 poits to life """
        self.player = player
        while self.player.mana > 9:
            self.player.life += 50
            self.player.mana -= 10
            print(f"vous avez recuperez de la santé vous avez {self.player.life} hp")
            time.sleep(2)
            os.system('cls||clear')

            return
        if self.player.mana <10:
            print("vous n'avez plus de mana !!")
            time.sleep(2)
            os.system('cls||clear')
