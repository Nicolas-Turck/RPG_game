import os
from game.factory import Program
from game.arena import Arena

if __name__=='__main__':

    player = Program()
    player.user_choice()
    player = player.import_player_heros()
    print(player.__dict__)
    rival = Program()
    rival.random_list()
    rival = rival.import_program_hero()
    print(rival.__dict__)
    game = Arena(rival, player)
    while player.life > 0  or rival.life > 0:
        game.action(rival, player)
        
        if player.life <= 0:
            print("finish you die you join biggi and tupac")
            break
        if rival.life <= 0:
            print("you win you saved mixity")
            break
        if game.player_choice == "a":
            game.calc_life(player,rival)
            game.rival_attack(player,rival)
        if game.player_choice == "r":
            game.run_or_fight(player, rival)