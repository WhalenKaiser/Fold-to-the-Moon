import math
import moonFold_test

def fold_to(distance):
    #your code her
    paper = 0.00005
    if distance <= 0:
        return None
    elif distance <= paper:
        return 0
    else:
        if paper == distance:
            return 0
        else:
            fold = 0
            while paper < distance:
                paper = paper * 2
                fold += 1
            return fold-1
