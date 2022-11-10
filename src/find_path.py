from src.move_board import *
from collections import deque
   

def game_won(board):
    num_tiles = 0
    
    for i in range(0, len(board)):
        for j  in range(0, len(board)):
            if (board[i][j] not in [0, 2048]):
                num_tiles += 1
            
    
    return True if num_tiles == 1 else False

def generate_key(board):
    key = ""
    
    for i in range(len(board)):
        for j in range(len(board)):
            key += (str(board[i][j]) + ",")
        key+="|"
        
    return str(key)


def find_path_bfs(board):
    queue = deque( [(board, "")] )
    visited = set()
    visited.add(generate_key(board))
    
    movement_funcs = [move_board_up, move_board_right, move_board_down, move_board_left] 

    while queue:
        state, moves = queue.popleft()
    
        if game_won(state):
            return moves 

    
        for direction, move, in enumerate(movement_funcs, start=1):
            moved_board = move(state)
            if generate_key(moved_board) not in visited:
                queue.append( (moved_board, moves + str(direction)) ) 
                visited.add(generate_key(moved_board))

    return "impossible"

        
        
