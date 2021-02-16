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

def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("------- -------- -------")
        
        for s in range(len(board[i])):
            if s % 3 == 0 and s != 0:
                print(" | ", end="")
            if s == 8:
                print(board[i][s])
            else:
                print(str(board[i][s]) + " ", end="")


def findAllEmpty(baord):
    for i in range(len(board)):
        for s in range(len(board[i])):
            if board[i][s] == 0:
                nextEmptyCord = (i+1, s+1) #print row and column of empty field
                print(nextEmptyCord)

printBoard(board)
findAllEmpty(board)
