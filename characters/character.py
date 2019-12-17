class Person:
    """commune class for all personnage of game """
    personnage = ["archer", "magicien", "guerrier"]
    ennemis = ["orc", "loup", "zombie"]

    def __init__(self, life, attack, defense, agility, name= False):
        self.life = life
        self.attack = attack
        self.defense = defense
        self.agility = agility

    def player_choice(self):
        choice = print()

    def enter_name(self, name):
        name = input("enter your name friends:")