player_name = input('What is your name? ')
print('-\nHello, ' + player_name + '. You see two doors in front of you. Red and blue.')

while True :
    door_picked = input('Which do you choose? ')
    if door_picked == 'red' :
        print('-\n-\nThe door opened, triggering an arrow trap!')
        print('You died.\n\n')
        exit()
    elif door_picked == 'blue' :
        start = 0
        print('-\n-\nThe door leads to a dark, open room.')
        print('You cannot tell how large the room is or if there are any threats.')
        print('Do you walk slowly forward or do you sprint as quickly as possible\nto the other side of the room?')
    elif door_picked == 'exit' :
        exit()
    elif not door_picked == 'red' or not door_picked == 'blue' :
        print('-\nI do not understand ' + door_picked + '.\n-')
        continue

    while True :
        choice_1 = input('Slow or fast? ')
        if choice_1 == 'slow' :
            print('-\n-\nA skeleton sneaks up behind you and decapitates you!')
            print('You died.\n\n')
            exit()
        elif choice_1 == 'fast' :
            print('-\n-\nYou begin sprinting, now realizing that you were about\nto be killed by a skeleton.')
            print('You run past several other skeletons that begin to run towards you.')
            print('After a few seconds of running through the darkness,\nyou come across another door.')
            print('Do you try and open the door or do you try and defeat the skeletons?')
        elif choice_1 == 'exit' :
            exit()
        elif not choice_1 == 'slow' or not choice_1 == 'fast' :
            print('-\nI do not understand ' + choice_1 + '.\n-')
            continue

        while True :
            choice_2 = input('Open door or fight skeletons? ')
            if choice_2 == 'fight skeletons' :
                print('-\n-\nYou bravely turn around, sword in hand, ready\nto fight your way through the horde.')
                print('You manage to take out one skeleton,\nand then another, before tripping over your own feet.')
                print('As you fall to the ground, you find yourself\nbeing surrounded on all sides by skeletons.')
                print('Before you can get your bearings, you feel the burning\npain of that of an old, rusted sword being\nthrust directly through your chest.')
                print('You died.\n\n')
                exit()
            elif choice_2 == 'open door' :
                print('-\n-\nLuckily the door opens, and you sprint in as\nquickly as possible, making sure to slam the door behind you.')
                print('You find yourself in a throne room.\nAll by its lonesome, sitting on the throne itself,\nis the crown of Yhorm.')
                print('You triumphantly walk over to the throne and\nbegin to claim your prize before hesitating.')
                print('-\n-\nYou quickly realize that this could be a trap.')
            elif choice_2 == 'exit' :
                exit()
            elif not choice_2 == 'open door' or not choice_2 == 'fight skeletons' :
                print('-\nI do not understand ' + choice_2 + '.\n-')
                continue

            while True :
                choice_3 = input('Do you take the crown or stop and think? ')
                if choice_3 == 'take the crown' :
                    print('You disregard any sub-thought and yank the crown.')
                    print('-\n-\nAlmost immediately the room begins to shake violently.')
                    print('You look up and see a grid of small openings in the ceiling.')
                    print('Before you can even comprehend what is happening,\nlong skewers fall from the openings in the ceiling\nimpaling you upon impact.')
                    print('You died.\n\n')
                    exit()
                elif choice_3 == 'stop and think' :
                    print('-\n-\nYou look around the room.')
                    print('This scenario seems all too familiar to you.')
                    print('You shuffle through the disarray, looking for a substitute.')
                    print('You end up taking a piece of rubble off of the ground\nand take it over to the throne.')
                    print('Now, ever so carefully, you swap the crown with a\nspeed and grace only rivaled by Indiana Jones.')
                    print('You pause...\n-\n-\n-\n-')
                    print('Phew, that was close!')
                    print('There is only one problem now: the skeletons.')
                elif choice_3 == 'exit' :
                    exit()
                elif not choice_3 == 'take the crown' or not choice_3 == 'stop and think' :
                    print('-\nI do not understand ' + choice_3 + '.\n-')
                    continue

                while True :
                    choice_4 = input('Do you run through the skeletons?\nOr do you try and take them out? ')
                    if choice_4 == 'run' :
                        print('-\n-\nYou open the door you came in, and are greeted\nby a hoard of skeletons, blocking your path out.')
                        print('You try and push through them, but are swiftly overpowered.')
                        print('The skeletons overwhelm you, and you find yourself\nsurrounded, unable to take them all on.')
                        print('They all charge at you, and take your life, just as theirs once were.')
                        print('You died.\n\n')
                        exit()
                    elif choice_4 == 'take them out' :
                        print('-\n-\nA sense of bravery fills you up, and you decide\nto put an end to those skeletons once and for all.')
                        print('You open the door and quickly run behind the throne.')
                        print('The skeletons begin to fill the room.\nThey must have not seen you, as they aimlessly\nwander around the seemingly empty room.')
                        print('You get an idea! You wait until all the skeletons\nhave entered the room and the doorway is clear.')
                        print('Once the coast is clear, you act on intuition and\nyank the crown substitute from the throne\nand begin running towards the open door.')
                        print('The room begins to rumble, but you make it out.\nYou slam the door behind you and hold it shut.')
                        print('You hear banging on the door before the sound of\nmetal violently striking the ground puts an end to it.')
                        print('You wait for a moment, to see if it all was done.\n-\n-\n-')
                        print('After a few seconds of silence, you open the door\nto find a pile of bones skewered by hundreds of metal spikes.')
                        print('The skeletons were defeated.\n-\n-')
                        print('You make your way out of the castle, with your prize.\n-\n-\n-\n-')
                        print('You win! Thanks for playing!\n\n')
                        exit()
                    elif choice_4 == 'exit' :
                        exit()
                    elif not choice_4 == 'run' or not choice_4 == 'take them out' :
                        print('-\nI do not understand ' + choice_4 + '.\n-')
                        continue
