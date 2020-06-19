import random


while True :
    inp = input('Enter how many sides you want your dice to have. Enter "exit" to quit. ')
    if inp == 'exit' :
        break

    sides = int(inp)
    dicesides = random.randint(1, sides)

    print(dicesides)
