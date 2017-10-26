from utils import ROCK, PAPER, SCISSORS, choice_list, get_player_choice, get_ai_choice

player_choice = get_player_choice()  # calling functions

ai_choice = get_ai_choice()  # random, list index
print "AI picked ", ai_choice

# if else conditionals
if player_choice == ai_choice:
    print "tie"
elif player_choice == ROCK and ai_choice == SCISSORS:
    print "win"
elif player_choice == SCISSORS and ai_choice == PAPER:
    print "win"
elif player_choice == PAPER and ai_choice == ROCK:
    print "win"
elif player_choice == SCISSORS and ai_choice == ROCK:
    print "lose"
elif player_choice == PAPER and ai_choice == SCISSORS:
    print "lose"
elif player_choice == ROCK and ai_choice == PAPER:
    print "lose"


# or:
if player_choice == ai_choice:
    print "tie"
elif (player_choice == ROCK and ai_choice == SCISSORS)\
        or (player_choice == SCISSORS and ai_choice == PAPER)\
        or (player_choice == PAPER and ai_choice == ROCK):
    print "win"
else:
    print "lose"
