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
        input = []

        for j in range(len(board)):
            input.append([board[j][i]])
            
        input = slide_up(input)
        input = combine_up(input)
        input = slide_up(input)
        
        
        for j in range(len(board)):
            moved_board[j][i] = input[j][0]
        
    return moved_board
        
        
def move_board_down(board):
    moved_board = board
    
    for i in range(len(board)):
        input = []

        for j in range(len(board)):
            input.append([board[j][i]])
            
        input = slide_down(input)
        input = combine_down(input)
        input = slide_down(input)
        
        
        for j in range(len(board)):
            moved_board[j][i] = input[j][0]
        
    return moved_board
    
    


    

    