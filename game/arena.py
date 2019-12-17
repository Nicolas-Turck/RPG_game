import random
ennemis = ["orc", "loup", "zombie"]
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


    def player_action(self):
        """"""
        len_life = True
        while len_life == True:
            while self.player_choice != "a" and self.player_choice != "r":
                self.player_choice = input("(a) for attack or (r) for run")
                print(self.player_choice)
                if self.player_choice == "a":
                    Arena.attack()

    def random_list():
        """method for choice ennemis """
        print(ennemis[random.randint(0, len(ennemis)-1)])




    def choice_player():
        #choice_players = input("attack (a) or run (r)")
        while choice_player != "a" or choice_player != "r":
            choice_players = input("attack (a) or run (r)")
            if choice_player == "a":
                print("your attacked ")
                attack()

            if choice_player == "r":
                print("you run ")
                run()




