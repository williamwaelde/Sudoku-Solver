# Game Board
# 0 = empty field
sudoku_board = [
    [7, 8, 0, 9, 0, 0, 3, 2, 0],
    [8, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 8, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 9, 5, 0, 9, 5, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 4, 0, 0, 0, 1, 2],
    [1, 2, 7, 8, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


#call recursively
def backtrackingAlgo(sb):
    #print progress for visualisation
    print(sb)

    find = find_empty_square(sb)

    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        #loop through val 0-9
        #check if adding it to board is a valid sultion
        if validCheck(sb, i, (row, col)):
            #valid is true = add to board
            sb[row][col] = i

            #call recursively with new value
            #break if found sultion or end of range = false
            if backtrackingAlgo(sb):
                return True
            #backtrack
            #last element reset because it is not valid
            #try with differnt value again
            sb[row][col] = 0
    return False
    print("- - - - - - -start- - - - - - -")


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


#find empty square (representet as on board)
def find_empty_square(sb):
    for i in range(len(sb)):
        for j in range(len(sb[0])):
            if sb[i][j] == 0:
                #return tupel row & col
                return (i, j)
    return None

#check if board is valid
def validCheck(sb, num, pos):
    #check row
    #if row value is equal to number added in
    for i in range(len(sb[0])):
        if sb[ pos[0] ][i] == num and pos[1] != i:
            return False

    #check col
    #if col value is equal to number added in
    for i in range(len(sb)):
        if sb[i][ pos[1] ] == num and pos[0] != i:
            return False

    #check field
    #division that results into whole number
    field_x = pos[1] // 3
    field_y = pos[0] // 3

    #loop though field
    #example: reach field with index 6
    #to get there: find current box and multiple by 3
    #from field 2: multiple by 3 to reach field 6
    #same for y value
    for i in range(field_y * 3, field_y * 3 + 3):
        for j in range(field_x * 3, field_x * 3 + 3):
            if sb[i][j] == num and (i,j) != pos:
                #found duplicate
                return False
    return True

#board before
print_sudokuBoard(sudoku_board)
print("- - - - - - - Start - - - - - - -")
#call backtracking algo
backtrackingAlgo(sudoku_board)
print("- - - - - - - End - - - - - - -")
print("- - - - - - - succsess - - - - - - -")
#board after algo
print_sudokuBoard(sudoku_board)
