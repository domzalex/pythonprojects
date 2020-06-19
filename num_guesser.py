import random

numrand = random.randint(0, 20)

total = 1
countdown = 4

print('Hello! This is Guess The Number. A random number will be generated and you will have 5 attempts to try and guess what that number is.')

while True :

    numin = int(input('Enter a number between 0 and 20: '))

    if countdown == 0 :
        print('Too bad! You lose!')
        break


    if numin == numrand :
        print('Your number: ' + str(numin))
        print('Random number: ' + str(numrand))
        print('Congrats! You guessed correctly!')
        print('Total number of guesses: ' + str(total))
        break
    elif numin > numrand :
        print('Your guess it too high! Try again!')
        total = total + 1
        countdown = countdown - 1
    elif numin < numrand :
        print('Your guess is too low! Try again!')
        total = total + 1
        countdown = countdown - 1
    else :
        continue
