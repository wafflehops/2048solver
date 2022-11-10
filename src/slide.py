def slide_right(row):
    left_bound = 0
    ans = []

    for i in range(len(row)):
        if row[i] == 2048:
            ans.append(_slide_right(row[left_bound:i]))
            left_bound = i + 1
            ans.append([2048])
    
    ans.append(_slide_right(row[left_bound:]))

    return [x for y in ans for x in y]


def _slide_right(row):
    filtered = list(filter(lambda x : (x != 0), row))
    
    return [0] * (len(row) - len(filtered)) + filtered


def slide_left(row):
    left_bound = 0
    ans = []

    for i in range(len(row)):
        if row[i] == 2048:
            ans.append(_slide_left(row[left_bound:i]))
            left_bound = i + 1
            ans.append([2048])
    
    ans.append(_slide_left(row[left_bound:]))

    return [x for y in ans for x in y]

    
def _slide_left(row):
    filtered = list(filter(lambda x : (x != 0), row))
    
    return filtered + [0] * (len(row) - len(filtered)) 

def slide_up(col):
    left_bound = 0
    ans = []

    for i in range(len(col)):
        if col[i][0] == 2048:
            ans.append(_slide_up(col[left_bound:i]))
            left_bound = i + 1
            ans.append( [[2048]] )
    
    ans.append(_slide_up(col[left_bound:]))

    return [x for y in ans for x in y]


def _slide_up(col):
    filtered = list(list(filter(lambda x : (x[0] != 0), col)))
    
    return filtered + [[0]] * (len(col) - len(filtered)) 

def slide_down(col):
    left_bound = 0
    ans = []

    for i in range(len(col)):
        if col[i][0] == 2048:
            ans.append(_slide_down(col[left_bound:i]))
            left_bound = i + 1
            ans.append( [[2048]] )
    
    ans.append(_slide_down(col[left_bound:]))

    return [x for y in ans for x in y]

def _slide_down(col):
    filtered = list(list(filter(lambda x : (x[0] != 0), col)))
    
    return [[0]] * (len(col) - len(filtered)) + filtered
    





