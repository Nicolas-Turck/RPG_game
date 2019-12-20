import os
import time 
from game.factory import Program
from game.storyAgent import Clear
from game.arena import Arena
from game.narrator import Narrator

if __name__=='__main__':

    narrator = Narrator()
    narrator.print()
    clear = Clear()
    player = Program()
    player.user_choice()
    clear.clear_screen()
    player = player.import_player_heros()
    narrator.show_informations(player)
    rival = Program()
    rival.random_list()
    rival = rival.import_program_hero()
    narrator.rival_informations(rival)
    time.sleep(5)
    os.system('cls||clear')
    clear.clear_screen()
    game = Arena(rival, player)
    # loops for game while player or rival is not dead
    while player.life > 0  or rival.life > 0:
        game.action(rival, player)
        clear.clear_screen()
        if player.life <= 0:
            print("Tu est mort tu rejoins Biggie et Tupac")
            break
        if rival.life <= 0:
            print("Tu gagne ")
            break
        if game.player_choice == "a":
            game.calc_life(player,rival)
            game.rival_attack(player, rival)
            clear.clear_screen()
        if game.player_choice == "r":
            game.run_or_fight(player, rival)
            clear.clear_screen()
        
        
