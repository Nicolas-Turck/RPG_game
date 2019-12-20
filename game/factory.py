import random
ennemis = ["orc", "loup", "zombie"]
personnage = ["archer", "magicien", "guerrier"]
class Program():
    
    ennemis = ["orc", "loup", "zombie"]
    personnage = ["archer", "magicien", "guerrier"]
    
    def __init__(self):
        self.name = None
        self.choice_hero = None
        self.program_player = None

    def user_choice(self):

        self.name = input("Veuillez entrer votre nom pour jouer :").upper()
        print(f"Bonne chance {self.name} le magnifique")
        print("Liste des heros disponible :  archer  (｀ʖ°)⊃🏹  🎯 , magicien (｀-´)⊃━☆ﾟ.*･｡ﾟ,      guerrier ︻╦̵̵͇̿̿̿̿╤── -- --")
        self.choice_hero=input("Veuillez choisir votre héro: ").lower()#player enter choice

    def import_player_heros(self):
        """method for create player hero and return it """
        if self.choice_hero == "archer":
            from characters.archer import Archer
            player = Archer(self.name)
            #print(player.__dict__)
            return player

        elif self.choice_hero == "guerrier":
            from characters.guerrier import Guerrier
            player = Guerrier(self.name)
            return player

        elif self.choice_hero == "magicien":
            from characters.magicien import Magicien
            player = Magicien(self.name)
            return player


    def random_list(self):
        """method for choice ennemis 
            with random method"""
        self.program_player = ennemis[random.randint(0, len(ennemis)-1)]
        print(self.program_player)
        self.choice_hero = self.program_player
        self.name = self.program_player
        #rival.import_program_hero(program_player)

    def import_program_hero(self):
        """method for create program player hero 
        if it choice with random and return it """
        
       

        if self.program_player == "orc":
            from characters.orc import Orc
            rival = Orc()
            #print(rival.__dict__)
            return rival

        elif self.program_player == "loup":
            from characters.loup import Loup
            rival = Loup()
            #print(rival.__dict__)
            return rival

        elif self.program_player == "zombie":
            from characters.zombie import Zombie
            rival = Zombie()
            #print(rival.__dict__)
            return rival