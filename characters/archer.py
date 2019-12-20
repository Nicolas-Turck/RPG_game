from .character import Person
class Archer(Person):
    """class for archer player"""
    def __init__(self, name):
        self.name = name
        super().__init__(350, 80, 30, 50, name)

    def heal(self, player):
        self.player = player
        print("Vous n'etes pas magicien!!")

