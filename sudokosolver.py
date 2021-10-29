# Game Board
# 0 = empty field
sudoku_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


# Output Gameboard
def print_sudokuBoard(sb):

 for i in range(len(sb)):
    #check if row is divisible with 3
    if i % 3 == 0 and i != 0:
        #draw horizontal line
        print("- - - - - - - - - - - - -")

    #check if it is the 3 element or multiple of 3
    for j in range(len(sb[0])):
        #draw vertical line
        if j % 3 == 0 and j != 0:
            print(" | ", end="")

        if j == 8:
            print(sb[i][j])
        else:
            print(str(sb[i][j]) + " ", end="")


print_sudokuBoard(sudoku_board)