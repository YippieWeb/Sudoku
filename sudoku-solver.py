import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,0]]

print(np.matrix(grid))

def possible(row, column, number):
    global grid 
    # is num in given row (scan left to right)
    for i in range(0,9):
        if grid[row][i] == number:
            return False

    # is num in given column (scan top to bottom)
    for i in range(0,9):
        if grid[i][column] == number:
            return False

    # num in given square
    x0 = (column // 3) * 3 # column 0,3,6
    y0 = (row // 3) * 3 # row 0,3,6

    for i in range(0,3): # two units leftwards
        for j in range(0,3): # two units rightwards
            if grid[y0+i][x0+j] == number:
                return False

    # num is not in row, column, or sq
    return True