from random import randrange

# we expect: Width == height
board = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
)

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



def enter_move(board, width, height):
    """
        Board - actual board status
        width - width of board
        height - height of board
    """

    maxValue = width * height

    try:
        nextMove = int(input("Please, enter your next move (number from: {} - {})".format(board[0][0], maxValue)))

        # If out of range
        if nextMove < 0 or nextMove > maxValue:
            print("You provided wrong value, please, try again.")
            return False

        

        return nextMove
    except ValueError:
        print("You provided wrong value, please, try again.")
        return False


# def make_list_of_free_fields(board):
#     # The function browses the board and builds a list of all the free squares; 
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.


# def victory_for(board, sign):
#     # The function analyzes the board's status in order to check if 
#     # the player using 'O's or 'X's has won the game


# def draw_move(board):
#     # The function draws the computer's move and updates the board.


display_board(board, boardWidth)

while not enter_move(board, boardWidth, boardHeight):
    print()
