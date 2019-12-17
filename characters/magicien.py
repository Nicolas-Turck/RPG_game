from characters.person import *

class Magicien(Person):
    """class for magicien player"""
    def __init__(self, name, life, attack, defense, agility):
        self.name = name
        self.mana = 50
        super().__init__(life, attack, defense, agility)