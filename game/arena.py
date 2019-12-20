import random
from game.factory import Program

ennemis = ["orc", "loup", "zombie"]
personnage = ["archer", "magicien", "guerrier"]
class Arena(Program):
    """class for create oject game """
    def __init__(self, rival, player, player_choice = None):
    
        self.player = player
        self.rival = rival

        self.player_choice = player_choice

    def action(self, rival, player):
        """method for choice action of game fight or run"""
        while self.player_choice != "a" or self.player_choice != "r":
            self.player_choice = input("(a) for attack or (r) for run..:").lower()
            if self.player_choice == "a":
                print("headshot")
                return

            if self.player_choice == "r" :
                print("Fuyezzzzzzzzzzz pauvre fou!!")
                return
                    
    def calc_life(self, player, rival):
        """method for calucalte lif if player choice combat"""
        if rival.defense > player.attack:
                dammages = rival.defense - player.attack
                rival.life -= dammages
                print(rival.life)
                  
        if rival.defense < player.attack:
            dammages = player.attack - rival.defense
            rival.life -= dammages
            print(rival.life)
       
    def run_or_fight(self, player, rival):
        """methode for use random for run if not good 
        go combat method calculate life after combat"""
        chance = random.randint(0, 50)
        print(chance)
        if chance == 49:
            print("ennemis distancer reprend ton souffle")
            return
        else:
            if player.defense > rival.attack:
                dammages = player.defense - rival.attack
                player.life -= dammages
                print(player.life)
            if player.defense < rival.attack:
                dammages = rival.attack - player.defense
                player.life -= dammages
                print(player.life)
        
            