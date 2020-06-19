import random


name = input('What is your name? ')
print('Good luck, ' + str(name) + '!')

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print('Guess a character: ')

guesses = ''
turns = 12

while turns > 0 :

    failed = 0

    for char in word :
        if char in guesses :
            print(char)
        else :
            print('_')
            failed = failed + 1

    if failed == 0 :
        print('You win!')
        print('The word is: ' + str(word))
        break

    guess = input('Guess a character: ')
    guesses += guess

    if guess not in word :
        turns = turns - 1
        print('Nope!')
        print('You have ' + str(turns) + ' more guesses.')

        if turns == 0 :
            print('Too bad. You lose!')
