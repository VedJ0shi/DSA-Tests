#recursively checks if a given str is a palindrome

def is_palindrome(phrase): 
    length = len(phrase)
    if length <= 1:
        return True

    first, last = phrase.casefold()[0], phrase.casefold()[length-1]
    if first == last: #checks if the first and last letter are same
        chopped = phrase[1:length-1]
        if is_palindrome(chopped):
            return True     
    return False
