class Person:
    """commune class for all personnage of game """

    def __init__(self, life, attack, defense, agility):
        self.life = life
        self.attack = attack
        self.defense = defense
        self.agility = agility

    def enter_name(self, name):
        name = input