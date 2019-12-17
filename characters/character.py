class Person:
    """commune class for all personnage of game """

    def __init__(self, life, attack, defense, agility, name= False):
        self.life = life
        self.attack = attack
        self.defense = defense
        self.agility = agility
