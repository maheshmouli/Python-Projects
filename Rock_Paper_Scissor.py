#Rock, Paper and Scissor game

import random

choices = ['Rock', 'Paper', 'Scissors']
computer = random.choice(choices)
player = False
CPU_score = 0
Player_score = 0

while True:
    player = input("Rock, paper, scissor?").capitalize()
    if player==computer:
        print('Tie!')
    elif player=='Rock':
        if computer=='Paper':
            print('You lose!', computer,'covers',player)
            CPU_score += 1
        else:
            print('You win!', player, "smashes", computer)
            Player_score += 1
    elif player == 'Paper':
        if computer=='Scissors':
            print('You lose!', computer,'cuts', player)
            CPU_score += 1
        else:
            print('You win!', player, 'covers', computer)
            Player_score += 1
    elif player == 'Scissors':
        if computer == 'Rock':
            print('You lose!', player, 'smashes', computer)
            CPU_score += 1
        else:
            print('You win!', player, 'cut', computer)
            Player_score += 1
    elif player=='End':
        print('=======Final Scores==========')
        print('CPU: {}'.format(CPU_score))
        print('Player:{}'.format(Player_score))
        break
