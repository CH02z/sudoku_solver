board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def printBoard(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("------- -------- -------")
        
        for s in range(len(bo[i])):
            if s % 3 == 0 and s != 0:
                print(" | ", end="")
            if s == 8:
                print(bo[i][s]) #at the last number of the row, print the number with a line Break
            else:
                print(str(bo[i][s]) + " ", end="") #Print the number without a line break (with a space instead)

def boardIsValid(bo, num, pos):
    # Is the Number appearing in the given row?
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Is the Number appearing in the given Column?
    for s in range(len(bo[0])):
        if bo[s][pos[1]] == num and pos[0] != s:
            return False

    # Is the number appearing in the Box

    # 1. Determine in wich square Number the position is:

    box_row = pos[0] // 3
    box_col = pos[1] // 3

    for i in range(box_col * 3, box_col * 3 + 3):
        for s in range(box_row * 3, box_row * 3 + 3):
            if bo[s][i] == num and (i, s) != pos:
                return False

    return True


def solve(bo):
    emptyField = findNextEmpty(bo)
    if not emptyField: # If emtpyfield is null, there are no empty fields left and the bard is solved
        return True
    else:
        row, col = emptyField

    for i in range(1,10):
        if boardIsValid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False
    

def findNextEmpty(bo):
    for i in range(len(bo)):
        for s in range(len(bo[i])):
            if bo[i][s] == 0:
                return (i, s) #Retun row and column of empty fields


print("")
print("")
printBoard(board)
solve(board)
print("")
print("------------------------")
print("")
printBoard(board)
print("")
print("")

