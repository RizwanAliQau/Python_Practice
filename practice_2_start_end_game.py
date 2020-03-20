game = ""
game1 = ""
while game.lower() != 'quit':
    game = input('>').lower()

    if game == 'help':
        print('''
        start- to start the game
        stop- to stopped.
        quit- to end the game''')
    elif game == 'start' and game1 != 'start':
        game1 = game
        print('car started...Ready to go')
    elif game == 'start' and game1 == 'start':
        print('the card already started')
    elif game == 'stop' and game1 != 'stop':
        game1 = game
        print('stop the car')
    elif game == 'stop' and game1 == 'stop':
        print('the card already stopped.')
    elif game == 'quit':
        break
    else:
        print("i don't understand that")
