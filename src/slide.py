def slide_right(row):
    filtered = list(filter(lambda x : (x is not 0), row))
    
    return [0] * (len(row) - len(filtered)) + filtered
    
    
def slide_left(row):
    filtered = list(filter(lambda x : (x is not 0), row))
    
    return filtered + [0] * (len(row) - len(filtered)) 


def slide_up(col):
    filtered = list(list(filter(lambda x : (x[0] is not 0), col)))
    
    return filtered + [[0]] * (len(col) - len(filtered)) 


def slide_down(col):
    filtered = list(list(filter(lambda x : (x[0] is not 0), col)))
    
    return [[0]] * (len(col) - len(filtered)) + filtered
    

    

