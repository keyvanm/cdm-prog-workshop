import random  # importing modules

# vars
ROCK = "r"
PAPER = "p"
SCISSORS = "s"

choice_list = [ROCK, PAPER, SCISSORS]  # small intro to lists


def get_player_choice():
    print "Please choose an option from r, p or s:"
    player_choice = raw_input()
    while player_choice not in choice_list:
        print "Please choose one of r, p or s:"
        player_choice = raw_input()
    return player_choice


def get_ai_choice():
    return choice_list[random.randint(0, 2)]


def check_who_won(player_choice, ai_choice):
    if player_choice == ai_choice:
        return 0
    elif (player_choice == "r" and ai_choice == "s")\
            or (player_choice == "s" and ai_choice == "p")\
            or (player_choice == "p" and ai_choice == "r"):
        return 1
    else:
        return -1
