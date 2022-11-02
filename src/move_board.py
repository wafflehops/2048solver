from slide import *
from combine import *

def move_board_right(board):
    moved_board = board
    
    for i in range(len(board)):
        moved_board[i] = slide_right(combine_right(slide_right(moved_board[i])))
    
    return moved_board


def move_board_left(board):
    moved_board = board
    
    for i in range(len(board)):
        moved_board[i] = slide_left(combine_left(slide_left(moved_board[i])))
    
    return moved_board


def move_board_up(board):
    moved_board = board
    
    for i in range(len(board)):
        col = [[board[x][i]] for x in range(0, len(board))]
            
        col = slide_up(combine_up(slide_up(col)))
        
        for j in range(len(board)):
            moved_board[j][i] = input[j][0]
        
    return moved_board
        
        
def move_board_down(board):
    moved_board = board
    
    for i in range(len(board)):
        col = [[board[x][i]] for x in range(0, len(board))]
        
        col = slide_down(combine_down(slide_down(col)))
        
        for j in range(len(board)):
            moved_board[j][i] = input[j][0]
        
    return moved_board
    
    


    

    