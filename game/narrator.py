class Narrator():

    def __init__(self):
        pass

    def show_informations(self, player):
        self.player = player
        print(f" {self.player.name}\n \
            Vous avez en points de vie: {self.player.life}\n \
            Votre puissance d'attaque et de {self.player.attack}\n \
            Votre défense est de {self.player.defense}")

    def rival_informations(self, rival):
        self.rival = rival
        print(f" {self.rival.name}\n \
            votre ennemis a  en points de vie: {self.rival.life}\n \
            votre ennemis a en puissance d'attaque  {self.rival.attack}\n \
            votre ennemis a en défense {self.rival.defense}")

    def start_game(self):
        print("	               _______ _______ _______")
        print("                      |   |   |    ___|    |  |")
        print("                      |       |    ___|       |")
        print("                      |__|_|__|_______|__|____|")
        print("  _______ ______ _______ _______    _______ _______ ______ _______ _______ ")
        print(" |    ___|   __ \       |   |   |  |    ___|   _   |   __ \_     _|   |   |")
        print(" |    ___|      <   -   |       |  |    ___|       |      < |   | |       |")
        print(" |___|   |___|__|_______|__|_|__|  |_______|___|___|___|__| |___| |___|___|")


        print("    ___ __ ")
        print("   (_  ( . ) )__                  '.    \   :   /    .'")
        print("     '(___(_____)      __           '.   \  :  /   .'")
        print("                     /. _\            '.  \ : /  .'")
        print("                .--.|/_/__      -----____   _  _____-----")
        print("_______________''.--o/___  \_______________(_)___________")
        print("       ~        /.'o|_o  '.|  ~                   ~   ~")
        print("  ~            |/    |_|  ~'         ~")
        print("               '  ~  |_|        ~       ~     ~     ~")
        print("      ~    ~          |_|O  ~                       ~")
        print("             ~     ___|_||_____     ~       ~    ~")
        print("   ~    ~      .'':. .|_|A:. ..::''.")
        print("             /:.  .:::|_|.\ .:.  :.:\   ~")
        print("  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~")
        print("             \.: .:  :. .: ..:: ./")
        print("    ~      ~      ~    ~    ~         ~")
        print("               ~           ~    ~   ~             ~")
        print("        ~         ~            ~   ~                 ~")
        print("   ~                  ~    ~ ~                 ~")

    def end_game(self):
        print("                              .___.")
        print("                     .ed#### ###$$$$be.")
        print("                   -#           ^##**$$$e.")
        print("                 .#                   '$$$c")
        print("                /                      #4$$b")
        print("               d  3                      $$$$")
        print("               $  *                   .$$$$$$")
        print("              .$  ^c           $$$$$e$$$$$$$$.")
        print("              d$L  4.         4$$$$$$$$$$$$$$b")
        print("              $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$")
        print("  e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$")
        print(" z$$b. ^c     3$$$F #$$$$b   $#$$$$$$$  $$$$*#      .=##$c")
        print("4$$$$L        $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$.")
        print("^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$")
        print("  #**$$$ec   #   %ce##    $$$  $$$$$$$$$$*    .r# =$$$$P##")
        print("        #*$b.  #c  *$e.    *** d$$$$$#L$$    .d#  e$$***#")
        print("          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*#.eeP")
        print("             #$$$$$$#'$=e....$*$$**$cz$$" "..d$*#")
        print("               #*$$$  *=%4.$ L L$ P3$$$F $$$P")
        print("                  #$   #%*ebJLzb$e$$$$$b $P")
        print("                    %..      4$$$$$$$$$$ ")
        print("                     $$$e   z$$$$$$$$$$%")
        print("                      #*$c  #$$$$$$$P")
        print("                       .###*$$$$$$$$bc")
        print("                    .-    .$***$$$###e. ")
        print("                 .-#    .e$#     #*$c  ^*b.")
        print("          .=*###   .e$*#          #*bc  #*$e..")
        print("        .$#        .z*#               ^*$e.   #*****e.")
        print("        $$ee$c   .d#                     #*$.        3.")
        print("        ^*$E#)$..$#                         *   .ee==d%")
        print("           $.d$$$*                           *  J$$$e*")
        print("            #####                              #$$$")
