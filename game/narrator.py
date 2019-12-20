class Narrator():

    def __init__(self):
        pass

    def show_informations(self, player):
        self.player = player
        print(f" {self.player.name}\n \
            vous avez en points de vie: {self.player.life}\n \
            votre puissance d'attaque et de {self.player.attack}\n \
            votre défense est de {self.player.defense}")

    def rival_informations(self, rival):
        self.rival = rival
        print(f" {self.rival.name}\n \
            votre ennemis a  en points de vie: {self.rival.life}\n \
            votre ennemis a en puissance d'attaque  {self.rival.attack}\n \
            votre ennemis a en défense {self.rival.defense}")