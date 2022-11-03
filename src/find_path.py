from move_board import *
from enum import Enum

class Moves(Enum):
    UP = "1"
    RIGHT = "2"
    DOWN = "3"
    LEFT = "4"
    

def game_won(board):
    num_tiles = 0
    
    for i in range(0, len(board)):
        for j  in range(0, len(board)):
            if (board[i][j] != None):
                num_tiles += 1
            
    
    return True if num_tiles == 1 else False

def get_key(board):
    key = ""
    
    for i in range(len(board)):
        for j in range(len(board)):
            key += (str(board[i][j]) + ",")
        key+=";"
        
    return key

def find_path(board):
    memo = {}
    return _find_path(board, "", 0, memo)

def _find_path(board, move_list, count, memo):
    if count > 13:
        return ""
    
    if game_won(board):
        return move_list
    
    min_moves = "111111111111"
    for move in Moves:
        if move == Moves.UP: moved_board = move_board_up(board)
        if move == Moves.RIGHT: moved_board = move_board_right(board)
        if move == Moves.DOWN: moved_board = move_board_down(board)
        if move == Moves.LEFT: moved_board = move_board_left(board)
        
        if moved_board == board: continue
        
        remaining_moves = _find_path(moved_board, move_list + move.value, count + 1, memo)
        
        print(move_list + move.value)
        if len(remaining_moves) < len(min_moves):
            min_moves = remaining_moves
        
    return min_moves
        

    
    
                
    
    

board = [
    [2, None, None, None],
    [2, None, None, None],
    [None, None, None, None],
    [None, None, None, None]
]










shortest_path = find_path(board)
print(shortest_path)

