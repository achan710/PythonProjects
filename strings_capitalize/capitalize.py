'''
https://www.hackerrank.com/challenges/capitalize
'''
def whitespace(c):
    if c == ' ' or c == '\t' or c == '\n':
        return True   
    return False
    
def capitalize(string):
    # attempt 1 - fails, because \t and \n are not handled
    # split string in tokens. call capitalize on all. join list back into string
    #tokens = string.split()
    #tokens = [str.capitalize(x) for x in tokens]
    #buffer = ' '.join(tokens)
    
    # attempt 2 - 1st try failed to set 1st character to upper(). add a chec
    # brute-force. walk entire string, look for whitespace(' ', '\t', '\n') and 
    # call upper() on next alphabet character

    buffer = ''
    flag_upper = False
    flag_start = True
    for s in string:
        if whitespace(s):
            # find whitespace
            flag_upper = True
        elif flag_upper:
            # try to set letter to upper case after whitespace
            s = s.upper()
            flag_upper = False
        elif flag_start == True:
            # try to set first letter of string to uppercase
            s = s.upper()
            flag_start = False
        buffer = buffer + s
    return buffer
    
if __name__ == '__main__':
    string = raw_input()
    capitalized_string = capitalize(string)
    print capitalized_string