def print_board(board):
    for row in board:
        for field in row:
            print('Q ', end='') if field else print('X ', end='')
        print()
    print()


def can_place_queen(board, row, col):
    for field in board[row]:
        if field: return False
    for i in range(len(board[0])):
        if board[i][col]: return False
    i, j = row, col
    l = len(board)
    while i < l and j < l:
        if board[i][j]: return False
        i, j = i + 1, j + 1
    i, j = row, col
    while i < l and j >= 0:
        if board[i][j]: return False
        i, j = i + 1, j - 1
    i, j = row, col
    while i >= 0 and j < l:
        if board[i][j]: return False
        i, j = i - 1, j + 1
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]: return False
        i, j = i - 1, j - 1
    return True

def place_queens(board, row=0):
    global nSolutions
    if row >= len(board):
        print_board(board)
        nSolutions += 1
        return
    for col, field in enumerate(board):
        if can_place_queen(board, row, col):
            board[row][col] = True
            place_queens(board, row + 1)
            board[row][col] = False


nSolutions = 0
# Note that [[False]*8]*8 does not work since * will just copy the address
# of the row!
board = [[False] * 8 for i in range(8)]
place_queens(board)
print("Found %s solutions!" % nSolutions)
python
