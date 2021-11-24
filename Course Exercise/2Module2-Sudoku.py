# 3 different functions 
# - checking row
# - checking column
# - checking 3x3 tile

from typing import Deque


def sudokuIsAlright(sudokuString: str)->bool:
    sudokuSize = 9
    row, column, square = "", {}, ""
    mistake = False

    for x in sudokuString:
        # skip break line
        if x == "\n":
            continue

        # check all chars in row - if same char found, set TRUE
        if row.find(x) != -1:
            mistake = True
            break

        row += x

        # if all chars checked, reset row
        if len(row) == sudokuSize:
            row = ""

    if mistake:
        return False

    for x in sudokuString:
        # skip break line
        if x == "\n":
            continue

        if 



            

# Should print yes
sudoku1 = """295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672"""

# Should print no
sudoku2 = """195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671"""

