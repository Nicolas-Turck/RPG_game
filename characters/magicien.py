from .character import Person


class Magicien(Person):
    """class for magicien player"""
    def __init__(self, name):
        self.name = name
        self.mana = 50
        super().__init__(600, 20, 50, 25, name)

    def heal(self, player):
        self.player = player
        while self.player.mana > 9:
            self.player.life += 50
            self.player.mana -= 10
            print (f"vous avez recuperez de la santé {self.player.life}hp")
            return
        if self.player.mana < 10:
                print("vous n'avez plus de mana")
            
