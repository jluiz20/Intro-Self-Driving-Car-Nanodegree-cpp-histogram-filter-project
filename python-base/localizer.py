import pdb
from helpers import normalize, blur

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    #
    # TODO - implement this in part 2
    for row in range(len(grid)):
        new_row = []
        for col in range(len(grid[0])):
            #calculate the new probability
            #pdb.set_trace()
            hit = grid[row][col] == color
            new_row.append(beliefs[row][col] * (hit * p_hit + (1-hit) * p_miss))
    
        new_beliefs.append(new_row)
    
    #sums all all the itens in the 2-D world
    totalSum = 0.
    for row in range(len(new_beliefs)):
        for col in range(len(new_beliefs[0])):
            totalSum+=new_beliefs[row][col]
    #normalize the values
    for row in range(len(new_beliefs)):
        for col in range(len(new_beliefs[0])):
            new_beliefs[row][col] /= totalSum
    
    return new_beliefs

def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height
            new_j = (j + dx ) % width
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)