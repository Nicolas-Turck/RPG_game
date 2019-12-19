import random
from game.factory import Program

ennemis = ["orc", "loup", "zombie"]
personnage = ["archer", "magicien", "guerrier"]
class Arena(Program):
    """"""
    personnage = ["archer", "magicien", "guerrier"]

    def __init__(self, rival, player, player_choice):

        self.program_player = rival
        self.user_player = player
        self.player_choice = player_choice
  
    def action(player_choice):
        player_choice = input("(a) for attack or (r) for run..:").lower()
        #while player.life > 0  and rival.life > 0:
        while player_choice != "a" or player_choice != "r":
            player_choice = input("(a) for attack or (r) for run..:").lower()
            
            if player_choice == "a":
                rival.life -= player.attack
                print(rival.life)
            if player_choice == "r" : 
                print("Fuyezzzzzzzzzzz pauvre fou!!")




