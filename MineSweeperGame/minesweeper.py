import random
import re

# create a board object to represent the minesweeper game
# this is so that we can just say "create a new board object", or
# "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        # keep track of these parameters
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        
        # create the board
        # helper function
        self.board = self.make_new_board() # plant the bombs
        self.assign_values_to_board()

        # initialize a set to keep track of which locations we've uncovered,
        #  we'll save (row, col) tupls into this set
        self.dug = set() #if we dig at 0, 0, then self.dug = {(0, 0)}

    
    def make_new_board(self):
        # construct a new board based on the dim size and num bombs
        # we should construct the list of lists here 
        # since we have a 2-D board, list of lists is more natural)

        # generate a new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1) #return a random integer N such that a <= N
            row = loc // self.dim_size #we want the number of times dim_size goes into loc to tell us
            col = loc % self.dim_size #we want the remainder to tell us what index in that row to look for

            if board[row][col] == '*':
                # this means we've planted a bomb there so keep going
                continue

            board[row][col] = '*' #plant the bomb
            bombs_planted += 1
        
        return board

    def assign_values_to_board(self):
        # now that bombs are planted, let's assign a number 0-8 for all the empty spaces, which represents how many neighboring bombs 
        # there are. we can precompute theses and it'll save us some effort checking what's around the board later on:
        # we are checking every row and every column
        for r in range(self.dim_size): #row index
            for c in range(self.dim_size): #column index
                if self.board[r][c] == '*':
                    # if this is already a bomb, we don't want to calculate anything
                    continue
                # if not fir this location on the board create a new function called get_num_neighboring_bombs
                # pass in the row and column index and then this function gieves the number of bombs surrounding
                # the row column
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        # iterate through each of the neighboring positions and sum number of bombs
        num_neighboring_bombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1): #for current row, check below and above
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1): #for current column, check left and right
                if r == row and c == col:
                    # this is our original location, don't check
                    continue
                if self.board[r][c] == '*': # there is a bomb at that location
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def dig(self, row, col):
        # dug at that location
        # return True if successful dig, false if bomb dug

        self.dug.add((row, col)) # keep track that we dug here

        if self.board[row][col] == '*': #there is a bomb
            return False
        elif self.board[row][col] > 0: #we dug at a location with neighboring bombs
            return True
        
        # self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1): #for current row, check below and above
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1): #for current column, check left and right
                if (r, c) in self.dug:
                    continue # don't dig where you've already dug
                self.dig(r, c)
        # if our initial dig didn't hit a bomb, we shouldn't hit a bomb here
        return True

    def __str__(self):
        # if you call print on this object, it'll print out what this function returns!
        # return a string that shows the board to the player

        # create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        # put this in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )
    
        # print the csv string
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '   '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'
        
        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

def play(dim_size=10, num_bombs=10):
    #Step 1: Create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    # Step 2: Show the user the board and ask where they want to dig
    
    # Step3a: if location is a bomb, show game over message
    # Step3b: if location is not a bomb, dig recursively until each square is at least next to a bomb
    # Step4: repeat steps 2 and 3a/b until there are no more plces to dig -> victory
    safe = True
    while len(board.dug) < board.dim_size **2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("where would you like to dig? Input as row, col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("invalid location. Try again.")
            continue
            
        # if it's valid, we dig
        safe = board.dig(row, col)
        if not safe:
            # dug a bomb
            break #game over

    #2 ways to end loop, let's check which one
    if safe:
        print("Congrats, you are victorious")
    else:    
        print("Sorry Game over")
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__': #good practice
    play()