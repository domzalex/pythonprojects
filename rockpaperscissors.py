import random

rps = ["rock", "paper", "scissors"]
wins = 0
losses = 0
draws = 0


while True :


    rand = random.choice(rps)
    move = input('Rock, Paper, Scissors... (Enter "exit" to quit and see totals): ')
    lmove = move.lower()

    if lmove == "exit" :
        print('Totals: W' + str(wins) + ' ' + 'L' + str(losses) + ' ' + 'D' + str(draws))
        break



    if not lmove in rps :
        print('Invalid move. Try again.')
        continue

    if lmove == rand :
        print('Your move: ' + move.capitalize())
        print('Bot move: ' + rand.capitalize())
        print('Draw! Go again!')
        draws = draws + 1
        continue
    elif lmove == "rock" and rand == "paper" :
        print('Your move: ' + move.capitalize())
        print('Bot move: ' + rand.capitalize())
        print('You lose!')
        losses = losses + 1
        continue
    elif lmove == "rock" and rand == "scissors" :
        print('Your move: ' + move.capitalize())
        print('Bot move: ' + rand.capitalize())
        print('You win!')
        wins = wins + 1
        continue
    elif lmove == "paper" and rand == "scissors" :
        print('Your move: ' + move.capitalize())
        print('Bot move: ' + rand.capitalize())
        print('You lose!')
        losses = losses + 1
        continue
    elif lmove == "paper" and rand == "rock" :
        print('Your move: ' + move.capitalize())
        print('Bot move: ' + rand.capitalize())
        print('You win!')
        wins = wins + 1
        continue
    elif lmove == "scissors" and rand == "rock" :
        print('Your move: ' + move.capitalize())
        print('Bot move: ' + rand.capitalize())
        print('You lose!')
        losses = losses + 1
        continue
    elif lmove == "scissors" and rand == "paper" :
        print('Your move: ' + move.capitalize())
        print('Bot move: ' + rand.capitalize())
        print('You win!')
        wins = wins + 1
        continue
