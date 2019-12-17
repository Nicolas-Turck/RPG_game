personnage = ["archer", "magicien", "guerrier"]
ennemis = ["orc", "loup", "zombie"]  

class Start():


    def __init__(self, choice_classes):
        self.choice_classes = choice_classes
   
    def enter_name():
        """ Ask name at player and loop if dont inform good name """
        name = input("Veuillez entrer votre nom pour jouer :")
        print("Bonne chance {}".format(name))
    
    def choice_hero():
        print("Liste des heros disponible :  archer ︻╦̵̵͇̿̿̿̿╤──,     magicien (∩｀-´)⊃━☆ﾟ.*･｡ﾟ,      guerrier (｀ʖ´)⊃-(==>")
        choice_classes=input("Veuillez choisir votre héro: ").lower()#player enter choice 
        while choice_classes not in personnage :
            print("Veuillez choisir entre archer, magicien ou guerrier") 
            choice_classes=input("Veuillez choisir votre héro: ").lower()#player enter choice 
        return choice_classes     