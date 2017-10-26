import random  # importing modules
from utils import ROCK, PAPER, SCISSORS, choice_list, get_player_choice, check_who_won, get_ai_choice


if __name__ == "__main__":
    player_score = 0  # accumulator 
    ai_score = 0

    for i in range(5):
        player_choice = get_player_choice()
        ai_choice = get_ai_choice()
        print "AI picked ", ai_choice

        who_won = check_who_won(player_choice, ai_choice)
        if who_won == 1:
            player_score += 1
            print "you won this round!"
        elif who_won == -1:
            ai_score +=1
            print "ai won this round!"
        else:
            print "tie this round"

    print "player final score: ", player_score
    print "ai final score: ", ai_score

    if player_score - ai_score > 0:
        print "you won the game!"
    elif player_score - ai_score < 0:
        print "ai won the game!"
    else:
        print "tie!"
