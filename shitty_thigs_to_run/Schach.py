gameboard = [['T2', 'k2', 'B2', 'Q2', 'K2', 'B2', 'k2', 'T2'],
             ['P2', 'P2', 'P2', 'P2', 'P2', 'P2', 'P2', 'P2'],
             ['00', '00', '00', '00', '00', '00', '00', '00'],
             ['00', '00', '00', '00', '00', '00', '00', '00'],
             ['00', '00', '00', '00', '00', '00', '00', '00'],
             ['00', '00', '00', '00', '00', '00', '00', '00'],
             ['P1', 'P1', 'P1', 'P1', 'P1', 'P1', 'P1', 'P1'],
             ['T1', 'k1', 'B1', 'Q1', 'K1', 'B1', 'k1', 'T1']]


def display_gameboard():
    print('\n                      player 0')
    print('(   1     2     3     4     5     6     7     8  ) colum\n')
    x = 1
    for rows in gameboard:
        print(x, rows)
        if x != 8:
            print('\n')
        x = x + 1

    print('r                     player 1\no\nw\ns\n')


def checkmove(startrow, startcolum, finishrow, finishcolum):
    global player
    gamepiece = gameboard[startrow][startcolum]
    movetogamepiece = gameboard[finishrow][finishcolum]
    gamepiceaffiliation = list(gamepiece)
    movetogamepiceaffiliation = list(movetogamepiece)

    if gamepiceaffiliation[1] == movetogamepiceaffiliation[1]:  # check if the number of the game pieces are the same
        print(
            'you can\'t remove your own game pieces try something else!')  # prevent the player from removing their own game pieces
        player = 1 - player
        return

    # -----------------pawn------------------------
    if gamepiece == 'P1':
        x = 1
        y = 6
        z = 2
    if gamepiece == 'P2':
        x = -1
        y = 1
        z = -2
    if startrow == y and startrow - finishrow == z and startcolum - finishcolum == 0 and movetogamepiece == '00':
        move(startrow, startcolum, finishrow, finishcolum, gamepiece)
    elif startrow - finishrow == x and startcolum - finishcolum == 0 and movetogamepiece == '00':
        move(startrow, startcolum, finishrow, finishcolum, gamepiece)
    elif startrow - finishrow == x and abs(
            startcolum - finishcolum) == 1 and movetogamepiece != '00':
        move(startrow, startcolum, finishrow, finishcolum, gamepiece)
    # -----------------tower-----------------------
    elif (gamepiece == 'T1' or gamepiece == 'T2') and (
            startrow - finishrow == 0 or startcolum - finishcolum == 0):  # check if tower moves straight
        something_in_the_way = False
        check_straight_blocked(startrow, startcolum, finishrow, finishcolum, gamepiece, something_in_the_way)
    # ------------------kight-----------------------------
    elif gamepiece == 'k1' or gamepiece == 'k2':
        if abs(startrow - finishrow) == 2 and abs(startcolum - finishcolum) == 1:  # check if the move is valid
            move(startrow, startcolum, finishrow, finishcolum, gamepiece)  # takes absolute amount check for both sides
        elif abs(startrow - finishrow) == 1 and abs(startcolum - finishcolum) == 2:
            move(startrow, startcolum, finishrow, finishcolum, gamepiece)
    # ------------------bishop------------------------------------
    elif (gamepiece in ("B1", "B2")) and abs(startrow - finishrow) - abs(
            startcolum - finishcolum) == 0:  # checks if bishop is moved and if the move is diagonal
        something_in_the_way = False
        check_diagonal_blocked(startrow, startcolum, finishrow, finishcolum, gamepiece, something_in_the_way)

    # ------------------king---------------------------------------
    elif (gamepiece in ('K1', 'K2')) and startcolum - finishcolum < 2 and startrow - finishrow < 2:
        move(startrow, startcolum, finishrow, finishcolum, gamepiece)

    # ------------------Queen---------------------------------------
    elif (gamepiece in ('Q1', 'Q2')) and ((startrow - finishrow == 0 or startcolum - finishcolum == 0)
                                        or abs(startrow - finishrow) - abs(startcolum - finishcolum) == 0):
        something_in_the_way = False
        check_straight_blocked(startrow, startcolum, finishrow, finishcolum, gamepiece, something_in_the_way)
        check_diagonal_blocked(startrow, startcolum, finishrow, finishcolum, gamepiece, something_in_the_way)
    else:
        print('you can\'t move like that!')
        player = 1 - player
    player = 1 - player


def check_straight_blocked(startrow, startcolum, finishrow, finishcolum, gamepiece, something_in_the_way):
    if startrow - finishrow == 0:  # check if move is horizontal
        for colums in range(abs(startcolum - finishcolum)):  # check if the move isn't blocked
            if startcolum - finishcolum > 0:
                if gameboard[startrow][startcolum - colums] != '00' and startcolum + colums != startcolum:
                    something_in_the_way = move_blocked(something_in_the_way)
            elif startcolum - finishcolum < 0:
                if gameboard[startrow][startcolum + colums] != '00' and startcolum + colums != startcolum:
                    something_in_the_way = move_blocked(something_in_the_way)
        if not something_in_the_way:
            move(startrow, startcolum, finishrow, finishcolum, gamepiece)

    if startcolum - finishcolum == 0:  # check if move is vertical
        for rows in range(abs(startrow - finishrow)):  # check if the move isn't blocked
            if startrow - finishrow > 0:
                if gameboard[startrow - rows][startcolum] != '00' and startrow + rows != startrow:
                    something_in_the_way = move_blocked(something_in_the_way)
            elif startrow - finishrow < 0:
                if gameboard[startrow + rows][startcolum] != '00' and startrow + rows != startrow:
                    something_in_the_way = move_blocked(something_in_the_way)
    if not something_in_the_way:
        move(startrow, startcolum, finishrow, finishcolum, gamepiece)


def check_diagonal_blocked(startrow, startcolum, finishrow, finishcolum, gamepiece, something_in_the_way):
    if startrow - finishrow > 0 and startcolum - finishcolum < 0:  # checks path clear right top
        for steps in range(abs(startrow - finishrow)):
            if steps != 0:
                if gameboard[startrow - steps][startcolum + steps] != '00':
                    something_in_the_way = move_blocked(something_in_the_way)

    elif startrow - finishrow > 0 and startcolum - finishcolum > 0:  # checks path clear left top
        for steps in range(abs(startrow - finishrow)):
            if steps != 0:
                if gameboard[startrow - steps][startcolum - steps] != '00':
                    something_in_the_way = move_blocked(something_in_the_way)

    elif startrow - finishrow < 0 and startcolum - finishcolum < 0:  # checks path clear right bottom
        for steps in range(abs(startrow - finishrow)):
            if steps != 0:
                if gameboard[startrow + steps][startcolum + steps] != '00':
                    something_in_the_way = move_blocked(something_in_the_way)

    elif startrow - finishrow < 0 and startcolum - finishcolum > 0:  # checks path clear right bottom
        for steps in range(abs(startrow - finishrow)):
            if steps != 0:
                if gameboard[startrow + steps][startcolum - steps] != '00':
                    something_in_the_way = move_blocked(something_in_the_way)

    if not something_in_the_way:
        move(startrow, startcolum, finishrow, finishcolum, gamepiece)


def move(startrow, startcolum, finishrow, finishcolum, gamepiece):
    gameboard[finishrow][finishcolum] = gamepiece
    gameboard[startrow][startcolum] = '00'
    display_gameboard()


def move_blocked(something_in_the_way):
    global player
    print('something is in the way!')
    player = 1 - player
    something_in_the_way = True
    return (something_in_the_way)


def player_move():
    while True:
        ''' sr = start row
                sc = start colum
                fr = finish row
                fc = finish colum
            '''
        # try:
        player_input_sr, player_input_sc, player_input_fr, player_input_fc = input(
            'player %d where do you want to move? (startrow,startcolum,finishrow,finishcolum):  ' % player).split()
        player_input_sr = int(player_input_sr) - 1  # minus 1 to match human intention with computer array
        player_input_sc = int(player_input_sc) - 1
        player_input_fr = int(player_input_fr) - 1
        player_input_fc = int(player_input_fc) - 1
        checkmove(player_input_sr, player_input_sc, player_input_fr, player_input_fc)
    # except:
    # print('ups! something went wrong .... good bye')
    # break


player = 1
display_gameboard()
player_move()
