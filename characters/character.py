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

    def enter_name():
        """ Ask name at player and loop if dont inform good name """
        name = input("Veuillez entrer votre nom pour jouer :")
        print("Bonne chance {}".format(name))

