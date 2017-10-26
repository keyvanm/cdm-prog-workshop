import utils

player_choice = utils.get_player_choice()
ai_choice = utils.get_ai_choice()

if player_choice == ai_choice:
    print "tie"
elif player_choice == "r" and ai_choice == "s":
    print "win"
elif player_choice == "s" and ai_choice == "p":
    print "win"
elif player_choice == "p" and ai_choice == "r":
    print "win"
else:
    print "lose"
