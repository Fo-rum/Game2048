from Tkinter import Frame, Label, CENTER

import LogicsFinal #importing the file containing the logic
import constants as c #importing the constants file


#here, Frame is the superclass
#inheriting the properties and the functions of the frame class
class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self) #Frame class needs the object on which it will be creating the frame
        
        self.grid() #Tknter contains the grid manager that allows us to visualize the widgets in the form of a grid
        #here, we can visualize the frame in the form of a grid
        #grid means rows&columns
        self.master.title('2048') #Everything in the frams class is a master
        self.master.bind("<Key>", self.key_down) #the frame will be binded. to see the UI, if any key is pressed then go to the key_down function
        
        #a map created for keys pressed and the function indicated
        self.commands = { c.KEY_UP: LogicsFinal.move_up, c.KEY_DOWN: LogicsFinal.move_down,
                         c.KEY_LEFT: LogicsFinal.move_left, c.KEY_RIGHT: LogicsFinal.move_right
            
                        }
        
        self.grid_cells = [] #grid contains cells. initially will be empty
        self.init_grid() #initialize the grid by adding widgets. actually creates the grid cells
        self.init_matrix() #add the widgets by calling this function. it will add the grid cells
        self.update_grid_cells() #intially all were zeros. if 2 comes, background and text color should be changed. It updates the UI and sets the color according to the numbers
    
        self.mainloop() #actually runs the program
        
    def init_grid(self):
        
        #inside the main Framegrid, we are creating one more frame of dimensions 400*400
        background = Frame(self, bg= c.BACKGROUND_COLOR_GAME,
                          width = c.SIZE, height = c.SIZE)
        
        background.grid() #creation of one grid inside another
        
        #inside the frame 16 cells have to be added.
        #GRID_LEN = 4 therefore i runs 4 loops and inner loop j also runs 4 times. So altogether 14 times
        for i in range(c.GRID_LEN):
            grid_row = [] 
            for j in range(c.GRID_LEN):
                cell = Frame(background,bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                            width= c.SIZE/c.GRID_LEN,
                            height= c.SIZE/c.GRID_LEN) #cell size = 400/4
                cell.grid(row=i, column=j,padx=c.GRID_PADDING,
                         pady=c.GRID_PADDING) #adding a cell in the grid at a particular position i,j
                t = Label(master=cell,text="",
                         bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                         justify=CENTER,font= c.FONT, width=5,height=2) #label is the text inside the cell
                
                t.grid() #visualized the label as a grid
                grid_row.append(t) #appending the labels
                
            self.grid_cells.append(grid_row) #[L1,L2,L3,L4],[L5,L6,L7,L8]...[L13,L14,L15,L16]
        
    
    def init_matrix(self):
        
        #internal matrix maintained and changes will be made in it
        self.matrix = LogicsFinal.start_game()
        LogicsFinal.add_new_two(self.matrix)
        LogicsFinal.add_new_two(self.matrix)
        
    
    def update_grid_cells(self):
        
        #using the internal matrix maintained, all the changes that wil be made in the matrix
        #will be reflected in the UI
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j] #get the (i,j) element from the matrix
                
                #if the element is 0, then keep the corresponding text in the grid empty and its background color empty too
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                    text="", bg= c.BACKGROUND_COLOR_CELL_EMPTY)
                
                #if it is not 0 then set the text of the corresponding cell to the number
                #and also set its background & foreground color by getting it from the dictionary mapped.
                else:
                    self.grid_cells[i][j].configure(text=str(
                    new_number), bg=c.BACKGROUND_COLOR_DICT[new_number],
                    fg= c.CELL_COLOR_DICT[new_number])
                    
        self.update_idletasks() #setting the color might take sometime so it will wait till that particular task is finished
        
    def key_down(self,event):
        #key_down function takes two arguments: key & event
        #self = object called
        #event = key pressed i.e. w,s,a,d
        key = repr(event.char) #prints w,s,a,d accordingly
        if key in self.commands:
            
            #for every key pressed, call its corresponding function mapped and pass the matrix as an argument
            self.matrix, changed= self.commands[repr(event.char)](self.matrix)
            if changed:
                LogicsFinal.add_new_two(self.matrix)
                self.update_grid_cells()
                changed = False
                if LogicsFinal.get_current_state(self.matrix) == 'WON':
                    self.grid_cells[1][1].configure(
                    text="You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(
                    text="Win!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                
                if LogicsFinal.get_current_state(self.matrix) == 'LOST':
                    self.grid_cells[1][1].configure(
                    text= "You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(
                    text="Lose!", bg=c.BACKGROUND_COLOR_CELL_EMPTY)

gamegrid = Game2048()
        
        
        
        
        