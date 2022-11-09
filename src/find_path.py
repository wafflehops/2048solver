from src.move_board import *
from collections import deque
   

def game_won(board):
    num_tiles = 0
    
    for i in range(0, len(board)):
        for j  in range(0, len(board)):
            if (board[i][j] != 0):
                num_tiles += 1
            
    
    return True if num_tiles == 1 else False

def get_key(board):
    key = ""
    
    for i in range(len(board)):
        for j in range(len(board)):
            key += (str(board[i][j]) + ",")
        key+=";"
        
    return key

# def find_path_dfs(board):
#     memo = {}
#     return _find_path_dfs(board, Moves.SKIP, 0, memo)


# def _find_path_dfs(board, last_move, count, memo):
#     if count > 13:
#         return ""

#     if game_won(board):
#         return last_move.value
    
#     min_moves = "111111111111111"
#     for move in Moves:
#         if move == Moves.SKIP: continue
#         if move == Moves.UP: moved_board = move_board_up(board)
#         if move == Moves.RIGHT: moved_board = move_board_right(board)
#         if move == Moves.DOWN: moved_board = move_board_down(board)
#         if move == Moves.LEFT: moved_board = move_board_left(board)
        
#         if moved_board == board: continue
        
#         remaining_moves = _find_path_dfs(moved_board, move, count + 1, memo)
#         if remaining_moves == "": continue
        
        
#         if len(remaining_moves) < len(min_moves):
#             min_moves = remaining_moves
        
#     if min_moves == "":
#         return ""
#     else:
#         return last_move.value + min_moves if last_move.value != "5" else min_moves

def find_path_bfs(board):
    queue = deque( [(board, "")] )

    movement_funcs = [move_board_up, move_board_right, move_board_down, move_board_left] 
    
    while queue:
        state, moves = queue.popleft()
    
        if game_won(state):
            return moves 

        if len(moves) > 12:
            return "unsolvable within 12 moves"

        for direction, move, in enumerate(movement_funcs, start=1):
            queue.append( (move(state), moves + str(direction)) )

        
        
