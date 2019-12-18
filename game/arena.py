import random
from game.factory import Program

ennemis = ["orc", "loup", "zombie"]
personnage = ["archer", "magicien", "guerrier"]
class Arena(Program):
    """"""
    personnage = ["archer", "magicien", "guerrier"]


    def __init__(self):

        self.program_player = rival
        self.user_player = player
        player_choice = player_choice
    
  

    def action():
        """"""
        while player.life > 0  or rival.life > 0:
            player_choice = input("(a) for attack or (r) for run..:")
            while player_choice != "a" or player_choice != "r":
                player_choice = input("(a) for attack or (r) for run..:")
                print(player_choice)
            if player_choice == "a":
                rival.life -= player.attack
                print(rival.life)





