import random
from game.factory import Program

class Arena(Program):
    """class for create oject game """
    def __init__(self, rival, player, player_choice = None):
    
        self.player = player
        self.rival = rival
        self.player_choice = player_choice

    def action(self, rival, player):
        """method for choice action of game fight or run"""
        while self.player_choice != "a" or self.player_choice != "r":
            self.player_choice = input("(a) pour attaquer, (r) pour s'enfuire ou (s) pour ce soigné:").lower()
            if self.player_choice == "s":
                mag = player.heal(player)          
            if self.player_choice == "a":
                print("headshot")
                return

            if self.player_choice == "r" :
                print("Fuyezzzzzzzzzzz pauvre fou!!")
                return

    def calc_life(self, player, rival):
        """method for calucalte lif if player choice combat"""
        critique = random.randint(0, 10)
        if critique == 10:
            dammages = player.attack
            rival.life -= dammages
            print(f"Vous mettez un coup spécial {self.rival.life} hp")
            return
        else:
            if rival.defense > player.attack:
                dammages = rival.defense - player.attack
                rival.life -= dammages
                print(f"la vie de votre adversaire est de {self.rival.life} hp")
                  
            if rival.defense < player.attack:
                dammages = player.attack /2
                rival.life -= dammages
                print(f"la vie de votre adversaire est de {self.rival.life} hp")

    def rival_attack(self, player, rival):
        """method for calucalte lif if player choice combat"""
        critique = random.randint(0, 10)
        if critique == 10:
            dammages = rival.attack
            player.life -= dammages
            print(f"Il vous met un coup spécial {self.player.life} hp")
            return
        else:
            if player.defense > rival.attack:
                dammages = player.defense - rival.attack
                player.life -= dammages
                print(f"l'adversaire contre attaque il vous touche vous avez {self.player.life} hp")
                  
            if player.defense < rival.attack:
                dammages = rival.attack /2
                player.life -= dammages
                print(f"l'adversaire contre attaque il vous touche vous avez {self.player.life} hp")
       
    def run_or_fight(self, player, rival):
        """methode for use random for run if not good 
        go combat method calculate life after combat"""
        chance = random.randint(0, 50)
        if chance == 49:
            print("Ennemis distancer reprend ton souffle")
            return
        else:
            if player.defense > rival.attack:
                dammages = player.defense - rival.attack
                player.life -= dammages
                print(f"Il vous rattrape et vous frappe, votre vie descend à {self.player.life} hp\nOn ne fuis pas une bagarre !")
            if player.defense < rival.attack:
                dammages = rival.attack - player.defense
                player.life -= dammages
                print(f"Il vous rattrape et vous frappe, votre vie descend à {self.player.life} hp\nOn ne fuis pas une bagarre !")
        
            