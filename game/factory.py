import random
ennemis = ["orc", "loup", "zombie"]
personnage = ["archer", "magicien", "guerrier"]
class Program():
    
    def __init__(self):

        player_choice = player_choice
        choice_classes = choice_classes
        self.rival = rival
        self.player = player
        name = name
    def enter_name():
        """ Ask name at player and loop if dont inform good name """
        
        name = input("Veuillez entrer votre nom pour jouer :").upper()
        
        print(f"Bonne chance {name} le magnifique")
        Program.choice_hero(name)
    
    def choice_hero(name):
        
        """method for player choice is hero"""
        
        print("Liste des heros disponible :  archer  (｀ʖ°)⊃🏹  🎯 , magicien (｀-´)⊃━☆ﾟ.*･｡ﾟ,      guerrier ︻╦̵̵͇̿̿̿̿╤── -- --")
        choice_classes=input("Veuillez choisir votre héro: ").lower()#player enter choice 
        while choice_classes not in personnage :

            choice_classes=input("Veuillez choisir votre héro: ").lower()#player enter choice 
        Program.import_player_heros(choice_classes, name)
    

    def random_list():
        """method for choice ennemis 
        with random method"""
        
        program_player = ennemis[random.randint(0, len(ennemis)-1)]
        Program.import_program_hero(program_player)

    def import_program_hero(program_player):
        """method for create program player hero 
        if it choice with random and return it """

        if program_player == "orc":
            from characters.orc import Orc
            rival = Orc()
            print(rival.__dict__)
            return rival

        if program_player == "loup":
            from characters.loup import Loup
            rival = Loup()
            print(rival.__dict__)
            return rival

        if program_player == "zombie":
            from characters.zombie import Zombie
            rival = Zombie()
            print(rival.__dict__)
            return rival


    def import_player_heros(choice_classes, name):
        """method for create player hero and return it """
        if choice_classes == "archer":
            from characters.archer import Archer
            player = Archer(name)
            print(player.__dict__)
            return player

        if choice_classes == "guerrier":
            from characters.guerrier import Guerrier
            player = Guerrier(name)
            print(player.__dict__)
            return player

        if choice_classes == "magicien":
            from characters.magicien import Magicien
            player = Magicien(name)
            print(player.__dict__)
            return player