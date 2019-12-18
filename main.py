import os
#from characters.character import Person
from game.factory import Program
#from characters.magicien import Magicien
#from characters.orc import Orc
#from characters.loup import Loup
#from characters.zombie import Zombie
#from characters.guerrier import Guerrier
#from characters.archer import Archer
from game.arena import Arena

if __name__=='__main__':


    Program.enter_name()
    Program.random_list()
    #print(player.__dict__)
    print("go to the fight for liberty")
    
    Arena.action()

    """slt Farid 
    comme je t'est expliquer j'ai un peu modifier le code 
    afin qu'il soit mieux ranger 
    j'ai cree deux methode pour cree deux joueur en fonction de la methode random 
    et de la methode du choix du heros les methodes que tu a fait hier ce sont les methodes
    import_program_hero 
    et 
    import_player_heros 
    de la class program 
    elle renvoie chacune un objet  (rival) pour l'une et (player) pour l'autre 
    creer avec les caracteristiques 
    de la classe de joueur choisie archer, zombie, guerrier...ect
     """

    """il reste a voir comment recuper les deux object (player) et (rival) qui sont crees dans la classe 
    Program du fichier factory afin de les utiliser dans la class arena du fichier arena 
    pour commencer le combat avec la methode action
    afin de pouvoir calculer les point de vie et finir le jeux """

    """cependant il n'y a pas beaucoup d'object ni beaucoup de self si j'ai le temps 
    je vais voir pour utiliser plus l'objet et les methodes getter et setter 
    que j'avais tenter mais que j'ai du enlever"""

    """dans l'etat le programme fonctionne jusqu'a l'appelle de la function Arena.action() ici dans le main ligne 19
    il y a deux print qui s'affiche en lancant le programme pour bien verifier que le choix du joueur et du program ressorte
    bien les object choisie cree"""

    """si sa te dit de continuer sur ce modele ci le mieux c'est que tu recupere tous en supprimant avent 
    ce qu'il y a sur ton pc et ensuite recuperer ma branche nicolas
    ou sinon on continue sur ce que l'on avait commencer ensemble dans ce cas la je recuperai ton travail"""

    """desoler si j'ai pas etais tres clair ou si le code et difficilement compréhensible bon courage nicos"""


    

