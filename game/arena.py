import random
class Combat():
    choice = ["attack", "run", ]
    personnage = ["archer", "magicien", "guerrier"]
    ennemis = ["orc", "loup", "zombie"]

    def __init__(self):
        choice_player = ""
        choice = choice


    def random_enemis(self):
        self.choice = random.randrange(1, 3)
        self.ennemis = random;randrange(0, 3)
        print(ennemis)



    def choice_player(self):
        while choice_player != "a" or choice_player != "r":
            choice_player = input("attack (a) or run (r) : ")

            if choice_player == "a":
                print("your attacked ")
                attack()

            if choice_player == "r":
                print("you run ")
                run()


    #def attack(self):



    #def run(self):

