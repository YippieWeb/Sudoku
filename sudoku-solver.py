import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

print(np.matrix(grid))

def possible(row, col, num):
    global grid 
    # is num in given row (scan left to right)
    for i in range(9):
        if grid[row][i] == num:
            return False

    # is num in given column (scan top to bottom)
    for i in range(9):
        if grid[i][col] == num:
            return False

    # num in given square
    x0 = (col // 3) * 3 # column 0,3,6
    y0 = (row // 3) * 3 # row 0,3,6

    for i in range(3): # two units rightwards
        for j in range(3): # two units downwards
            if grid[y0+i][x0+j] == num:
                return False

    # num is not in row, column, or sq
    return True

def solve():
    global grid
    for row in range(9): #0-8
        for col in range(9):
            if grid[row][col] == 0: # if blank
                for num in range(1,10): #1-9
                    if possible(row, col, num):
                        grid[row][col] = num
                        solve() # recursive call
                        grid[row][col] = 0
                
                return
    
    print(np.matrix(grid))
    input('More?')

solve()
