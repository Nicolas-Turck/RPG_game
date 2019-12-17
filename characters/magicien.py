from .character import Person

class Magicien(Person):
    """class for magicien player"""
    def __init__(self, name):
        self.name = name
        #self.mana = 50
        super().__init__(600, 20, 50, 25, name)