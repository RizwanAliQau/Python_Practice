game = ""
while game.lower() != 'quit':
    game = input('>').lower()
    if game == 'help':
        print('''
        start- to start the game
        stop- to stopped.
        quit- to end the game''')
    elif game == 'start':
        print('car started...Ready to go')
    elif game == 'stop':
        print('stop the car')
    elif game == 'quit':
        break
    else:
        print("i don't understand that")
