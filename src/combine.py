def combine_right(row):
    combined_row = row[:]
    
    for i in range(len(combined_row) - 1, 0, -1):
        if combined_row[i] == combined_row[i - 1] and combined_row[i] != 2048:
            combined_row[i] *= 2
            combined_row[i - 1] = 0
    
    return combined_row

def combine_left(row):
    combined_row = row[:]
    
    for i in range(0, len(combined_row) - 1):
        if combined_row[i] == combined_row[i + 1] and combined_row[i] != 2048:
            combined_row[i] *= 2
            combined_row[i + 1] = 0
    
    return combined_row
        

def combine_up(col):
    combined_col = [row[:] for row in col]
    
    for i in range (0, len(combined_col) - 1):
        if combined_col[i][0] == combined_col[i + 1][0] and combined_col[i][0] != 2048:
            combined_col[i][0] *= 2
            combined_col[i + 1][0] = 0
            
    
    return combined_col

def combine_down(col):
    combined_col = [row[:] for row in col]
    
    for i in range (len(combined_col) - 1, 0, -1):
        if combined_col[i][0] == combined_col[i - 1][0] and combined_col[i][0] != 2048:
            combined_col[i][0] *= 2
            combined_col[i - 1][0] = 0
            
    
    return combined_col
        
