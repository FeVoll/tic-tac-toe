board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


def showBoard(board):
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")


def move(board, playerSymbol, x, y):
    if x > 3 or x < 1 or y > 3 or y < 1:
        print('wrong cords')
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



def playerWin(board, playerSymbol):
    #проверка на линии по горизонтали
    for j in range(3):
        winSymbols = 0
        for i in range(3):
            if board[j][i] == playerSymbol:
                winSymbols += 1
        if winSymbols == 3:
            return True
    #Проверка на линии по вертикали
    for j in range(3):
        winSymbols = 0
        for i in range(3):
            if board[i][j] == playerSymbol:
                winSymbols += 1
        if winSymbols == 3:
            return True
    #Проверка на линии по диагонали

    winSymbols = 0
    for i, j in zip(range(3), range(3)):
        if board[i][j] == playerSymbol:
            winSymbols += 1
        if winSymbols == 3:
            return True

    winSymbols = 0
    for i in range(3):
        if board[0+i][2-i] == playerSymbol:
            winSymbols += 1
        if winSymbols == 3:
            return True


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

def game(board):
    movecount = 0
    while True:
        print('Input coords in format N M. Where N - row and M - column. Example: "1 3" for top right corner')
        coords = input().split()
        x = int(coords[0])
        y = int(coords[1])
        if movecount % 2 == 0:
            if move(board, 'X', x, y) == True:
                movecount += 1
        elif movecount % 2 == 1:
            if move(board, '0', x, y) == True:
                movecount += 1
        if gameOver(board) == True:
            print('Game over!')
            return




while True:
    game(board)
    print('Play again? 1 - yes / other - no')
    answer = input()
    if answer != '1':
        print('Bye bye :>')
        break
    elif answer == '1':
        board = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]
