from characters.person import *
class Guerrier(Person):
    """class for guerrier player"""
    def __init__(self, name, life, attack, defense, agility):
        self.name = name
        super().__init__(life, attack, defense, agility,)