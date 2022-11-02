from slide import *
from combine import *

def move_board_right(board):
    moved_board = board
    
    for i in range(len(board)):
        moved_board[i] = slide_right(moved_board[i])
        moved_board[i] = combine_right(moved_board[i])
        moved_board[i] = slide_right(moved_board[i])
    
    return moved_board


def move_board_left(board):
    moved_board = board
    
    for i in range(len(board)):
        moved_board[i] = slide_left(moved_board[i])
        moved_board[i] = combine_left(moved_board[i])
        moved_board[i] = slide_left(moved_board[i])
    
    return moved_board


def move_board_up(board):
    moved_board = board
    
    for i in range(len(board)):
        col = [[board[x][i]] for x in range(0, len(board))]
            
        col = slide_up(col)
        col = combine_up(col)
        col = slide_up(col)
        
        for j in range(len(board)):
            moved_board[j][i] = input[j][0]
        
    return moved_board
        
        
def move_board_down(board):
    moved_board = board
    
    for i in range(len(board)):
        col = [[board[x][i]] for x in range(0, len(board))]
        
        col = slide_down(col)
        col = combine_down(col)
        col = slide_down(col)
        
        for j in range(len(board)):
            moved_board[j][i] = input[j][0]
        
    return moved_board
    
    


    

    