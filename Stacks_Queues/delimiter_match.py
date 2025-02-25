#pushing chars of an arithmetic str to a Stack to see if delimiters are matched
from arraystack import Empty, ArrayStack

def is_matched(expr):
    '''returns true iff all delimiters are matched'''
    delimiters = ('({[', ')}]')
    S = ArrayStack() #tracks opening delimiter symbols only

    for char in expr:
        if char in delimiters[0]: #opening delimiters
            S.push(char)
        elif char in delimiters[1]: #closing delimiters
            j = delimiters[1].index(char)
            if S.is_empty(): 
                return False #cannot begin expr with closing delimiter
            if S.pop() != delimiters[0][j]: #if top of stack is not the matching opening delim
                return False          
    return S.is_empty() #were all opening symbols even closed?
