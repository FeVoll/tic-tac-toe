board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


# 1.1
def showEmptyBoard():
    for i in range(3):
        print("|   |   |   |")


# 1.2
def showBoard(board):
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")


# 1.3
def move(board, playerSymbol, x, y):
    if x > 3 or x < 1 or y > 3 or y < 1:
        print('Wrong coords')
        showBoard(board)
        return False
    else:
        if board[x - 1][y - 1] == ' ':
            board[x - 1][y - 1] = playerSymbol
            showBoard(board)
            return True
        else:
            print('Try another')
            showBoard(board)
            return False


# 1.4
def playerWin(board, playerSymbol):

    for j in range(3):
        winSymbols = 0
        for i in range(3):
            if board[j][i] == playerSymbol:
                winSymbols += 1
        if winSymbols == 3:
            return True

    for j in range(3):
        winSymbols = 0
        for i in range(3):
            if board[i][j] == playerSymbol:
                winSymbols += 1
        if winSymbols == 3:
            return True


    winSymbols = 0
    for i, j in zip(range(3), range(3)):
        if board[i][j] == playerSymbol:
            winSymbols += 1
        if winSymbols == 3:
            return True

    winSymbols = 0
    for i in range(3):
        if board[0 + i][2 - i] == playerSymbol:
            winSymbols += 1
        if winSymbols == 3:
            return True
    else:
        return False


# 1.5
def gameOver(board):
    emptySlots = 9
    for x in range(3):
        for y in range(3):
            if board[x][y] != ' ':
                emptySlots -= 1
    if emptySlots == 0:
        print('No more slots')
        return True
    if playerWin(board, 'X') == True:
        print('Player X - wins')
        return True
    elif playerWin(board, '0') == True:
        print('Player 0 - wins')
        return True


# 1.6 (+ 2.3)
def game(board, fileUrl):
    movecount = 0
    while True:
        print('Do you want to load a saved game? 1 - yes 2 - no')
        loadChoose = input()
        if loadChoose == '1':
            try:
                board = loadBoard(fileUrl)
            except:
                print('There is no save file, save the game first')
            showBoard(board)
            break
        elif loadChoose == '2':
            break
    for x in range(3):
        for y in range(3):
            if board[x][y] != ' ':
                movecount += 1
    while True:
        if movecount % 2 == 0:
            print('Round', movecount + 1, '- Player X move.\n'
                                          'Input coords in format N M. Where N - row and M - column. Example: "1 3" for top right corner '
                                          'or write "save" to save the game')
            try:
                playerInput = input()
                if playerInput == 'save':
                    saveBoard(board, fileUrl)
                    return
                else:
                    coords = playerInput.split()
                    x = int(coords[0])
                    y = int(coords[1])
                    if move(board, 'X', x, y) == True:
                        movecount += 1
            except:
                print('Check your input and try again')

        elif movecount % 2 == 1:
            print('Round', movecount + 1, '- Player 0 move.\n'
                                          'Input coords in format N M. Where N - row and M - column. Example: "1 3" for top right corner '
                                          'or write "save" to save the game')
            try:
                playerInput = input()
                if playerInput == 'save':
                    saveBoard(board, fileUrl)
                    return
                else:
                    coords = playerInput.split()
                    x = int(coords[0])
                    y = int(coords[1])
                    if move(board, '0', x, y) == True:
                        movecount += 1
            except:
                print('Check your input and try again')
        if gameOver(board) == True:
            print('Game over!')
            return


# 2.1

def saveBoard(board, fileUrl):
    f = open(fileUrl, 'w')
    for x in board:
        f.write(str(x) + '\n')
    f.close()


# 2.2
def loadBoard(fileUrl):
    f = open(fileUrl, 'r')
    board = []
    board2 = []
    for line in f:
        board.append(str(line)[:-1])
    f.close()

    for x in range(3):
        board2.append(board[x][1:-1].split(', '))
        for y in range(3):
            board2[x][y] = board2[x][y][1:-1]

    return board2


while True:
    game(board, 'save.txt')
    print('Play again? 1 - yes / other - no')
    answer = input()
    if answer != '1':
        print('Bye bye :>')
        break
    elif answer == '1':
        board = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]
