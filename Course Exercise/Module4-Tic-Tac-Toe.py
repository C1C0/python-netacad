from random import randrange

userSymbol = "O"
computerSymbol = "X"

# we expect: Width == height
board = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)
fieldsList = []

try:
    # get width and height and check them, as they should be similar
    boardWidth = len(board)
    boardHeight = len(board[0])
except IndexError:
    print("Board has nothing inside, exiting program...")
    exit()
except:
    print("Unrecognized error occured.")
    exit()


# dimesions should be similar
if boardWidth != boardHeight:
    print("Board has different dimensions, exiting program...")
    exit()


def boardDivider(width):
    """
        if length 3 - then:\n
        +-------+-------+-------+
    """

    boardPart = ""
    for i in range(width):
        boardPart += "+-------"

        if i == width - 1:
            boardPart += "+"

    return boardPart

def boardNoCharSpace(width):
    """
        if length 3 - then:\n
        |sssssss|sssssss|sssssss|
    """

    boardPart = ""
    for i in range(width):
        boardPart += "|       "

        if i == width - 1:
            boardPart += "|"

    return boardPart

def boardCharSpace(row):
    """
        if length 3 - then:\n
        |sss1sss|sss2sss|sss3sss| 
    """

    boardPart = ""
    for i in range(len(row)):
        boardPart += "|   {}   ".format(row[i])

        if i == len(row) - 1:
            boardPart += "|"

    return boardPart

def display_board(board, width):
    '''
        board - board with same dimmension - basically two dimensionall list \n
        width - checked with of the board \n
        height - checked height of the board \n
    '''

    for row in board:
        print(boardDivider(width))
        print(boardNoCharSpace(width))
        print(boardCharSpace(row))
        print(boardNoCharSpace(width))

        # get last board divider - as border
        if board.index(row) == width - 1:
                print(boardDivider(width))



def enter_move(board, width, fieldsList):
    """
        Board - actual board status
        width - width of board
        height - height of board
    """

    maxValue = width * width

    try:
        nextMove = int(input("Please, enter your next move (number from: {} - {}): ".format(1, maxValue)))

        # If out of range
        if nextMove < 0 or nextMove > maxValue:
            print("You provided wrong value, please, try again.")
            return False

        nextMove -= 1

        row, i = fieldsList[nextMove]

        # check if not taken
        if type(board[row][i]) != int:
            print("This place is already taken, please, provide different number")
            return False

        board[row][i] = "O"

        return True
    except ValueError:
        print("You provided wrong value, please, try again.")
        return False


def make_list_of_free_fields(width):
    """
    Makes list of tuples with free places
    """

    availablePositions = []

    for row in range(width):
        for i in range(width):
            availablePositions.append((row, i))

    return availablePositions



def victory_for(board, width, sign):
    """
    The function analyzes the board's status in order to check if 
    the player using 'O's or 'X's has won the game
    """

    cross1 = cross2 = True

    for row in range(width):
        # check row
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return True

        # check column
        if board[0][row] == sign and board[1][row] == sign and board[2][row] == sign:
            return True

        # check diagonal from 1 to 9
        if board[row][row] != sign:
            cross1 = False

        # check diagonal from 3 to 7
        if board[2 - row][2 - row] != sign:
            cross2 = False

    print("Crosses:", cross1 or cross2)

    return cross1 or cross2    


def draw_move(board, width, fieldsList):
    """
    The function draws the computer's move and updates the board.
    """

    maxValue = width * width
    computerMove = randrange(maxValue)

    row, i = fieldsList[computerMove]

    computerMove -= 1

    # check if not taken
    if type(board[row][i]) != int:
        return False

    board[row][i] = "X"

    return True


fieldsList = make_list_of_free_fields(boardWidth)
winner = ""
numberOfMoves = 0
while True:
    if numberOfMoves > boardWidth * boardWidth:
        break

    # Computer Move
    while not draw_move(board, boardWidth, fieldsList):
        print(end="")
    
    if victory_for(board, boardWidth, computerSymbol):
        winner = "Computer"
        break

    # display
    display_board(board, boardWidth)

    # Players move
    while not enter_move(board, boardWidth, fieldsList):
        print()

    if victory_for(board, boardWidth, userSymbol):
        winner = "Player"
        break

    numberOfMoves += 2

display_board(board, boardWidth)
if winner == "":
    print("Tie")
else:
    print("The winner is", winner)