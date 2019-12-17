import random

class Arena():
    """"""
    personnage = ["archer", "magicien", "guerrier"]
    enn = ""
    len_life = True
    def __init__(self):
        self.choice = choice
        self.player_choice = player_choice
        self.ennemis = ennemis
        self.ennemis_liste = ["orc", "loup", "zombie"]

    def random_program(self):
        """"""
        self.choice = random.randrange(1, 4)
        return self.choice
        """for elem in self.ennemis_liste:
            if self.choice == elem[index]:
                self.ennemis = elem[index]
            print(self.ennemis)
            return self.choice
            return self.ennemis
            print(self.choice)
            print(self.ennemis)"""


    def player_action(self):
        """"""
        len_life = True
        while len_life == True:
            while self.player_choice != "a" and self.player_choice != "r":
                self.player_choice = input("(a) for attack or (r) for run")
                print(self.player_choice)
                if self.player_choice == "a":
                    Arena.attack()

    def attack(self):
        """"""
        print("contact")


