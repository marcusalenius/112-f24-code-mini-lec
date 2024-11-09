if True:
    import datetime
    def findFirstKnight(board):
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 1:
                    return (row, col)
        return None


### Keep lines under 80 characters ###

def isKnightsTour(board):
    # The board must be square
    rows = len(board)
    cols = len(board[0])
    if rows != cols:
        return False
        
    start = findFirstKnight(board)
    # There is no 1 in the board, so it can't be a valid knight's tour
    if start == None:
        return False

    # Ensure all moves are valid
    row, col = start
    moves = [(+2,+1), (+2,-1), (+1,+2), (+1,-2), 
             (-2,+1), (-2,-1), (-1,+2), (-1,-2)]
    for nextKnight in range(2, rows*cols + 1):
        foundNextKnight = False
        for drow, dcol in moves:
            newRow, newCol = row + drow, col + dcol
            if 0 <= newRow < rows and 0 <= newCol < cols and board[newRow][newCol] == nextKnight:
                row, col = newRow, newCol
                foundNextKnight = True
                print('Long message that I am printing indicating that the next knight was found right at this position')
        if not foundNextKnight:
            return False
    return True

