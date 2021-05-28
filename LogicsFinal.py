import random
def start_game():
    
    #initializing the matrix with all zeros
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat

def add_new_two(mat):
    #generate random position for 2
    
    row = random.randint(0,3) #generate random row
    column = random.randint(0,3) #generate random column
    
    #there is a need to find an empty position to insert 2
    #while loop continues till an empty block is found
    #0 present at particular position indicates empty space
    while(mat[row][column] != 0):
        row = random.randint(0,3) 
        column = random.randint(0,3)
    mat[row][column] = 2 #inserting 2 to the respective position
    
def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([]) #for every row,add a new list in the new matrix
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1]) #adding every element to specific row
            
    return new_mat

def transpose(mat):
    
    new_mat = []
    for i in range(4):
        new_mat.append([]) #for every row, a new empty list is added in the new matrix
        for j in range(4):
            #appending the new element in the i'th list
            #new element present actually at mat[j][i]
            #will be added in position new_mat[i][j]
            new_mat[i].append(mat[j][i])
    
    return new_mat

def merge(mat):
    #check for consecutive elements i.e j & j+1
    #if they are equal then add them otherwise move next
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j] * 2
                mat[i][j+1] = 0
                changed = True #if a match found, merge takes place and change has occured
                
    return mat,changed
            
    
def compress(mat):
    #pushing all the non-zeros to the left
    #having all the zeros to the right
    changed = False
    new_mat = []
    for i in range(4):
        new_mat.append([0]*4)
        
    for i in range(4):
        pos = 0 #for every row, initialize the position
        for j in range(4):
            if mat[i][j] != 0: 
                new_mat[i][pos] = mat[i][j] #filling row wise at particular position
                if j!= pos: #the row remains the same, but if column changes then this indicates a change has occured
                    changed = True #if for any row, the position of any element has changed that indicates a change has occured
                pos+=1
    
    return new_mat,changed

def move_down(grid):
    transposed_grid = transpose(grid)
    reversed_grid = reverse(transposed_grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_transposed_grid = transpose(final_reversed_grid)
    return final_transposed_grid,changed


def move_up(grid):
    transposed_grid = transpose(grid)
    new_grid,changed1 = compress(transposed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_grid = transpose(new_grid)
    return final_grid,changed

def move_right(grid):
    reversed_grid = reverse(grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp  = compress(new_grid)
    final_grid = reverse(new_grid)
    return final_grid,changed

def move_left(grid):
    
    new_grid,changed1 = compress(grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    return new_grid,changed

def get_current_state(mat):
    
    #checking every matrix block to find if we have won or not
    #Win the game - if 2048 is encountered in any block
    #Checking if anywhere 2048 is present
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 2048) :
                return 'WON'
     
    #reaching at this particular position, means either we are
    #in the game or have lost the game
    #Checking if anywhere 0 is present
    for i in range(4):
        for j in range(4):
            if (mat[i][j] == 0):
                return 'GAME NOT OVER'
    
    #Checking for every row and column
    #except for last row and last column
    for i in range(3):
        for j in range(3):
            if(mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]):
                return 'GAME NOT OVER'
    
    #Checking for the last row
    #fixing i and moving j
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return 'GAME NOT OVER'
        
    #Checking for the last column
    #fixing j and moving i
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return 'GAME NOT OVER'
        
    #No movement left hence game lost
    #No empty position or 2048
    return 'LOST'