def slide_right(row):
    filtered = list(filter(lambda x : (x is not None), row))
    
    return [None] * (len(row) - len(filtered)) + filtered
    
    
def slide_left(row):
    filtered = list(filter(lambda x : (x is not None), row))
    
    return filtered + [None] * (len(row) - len(filtered)) 


def slide_up(col):
    filtered = list(list(filter(lambda x : (x[0] is not None), col)))
    
    return filtered + [[None]] * (len(col) - len(filtered)) 


def slide_down(col):
    filtered = list(list(filter(lambda x : (x[0] is not None), col)))
    
    return [[None]] * (len(col) - len(filtered)) + filtered
    

    

