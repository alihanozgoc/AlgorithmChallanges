# Requirements:
# Every opening parenthesis must be closed.
# An unclosed parenthesis cannot be closed.

# Test Cases:
# Input             Output      Reason

# ()                True
# )(                False       An unclosed parenthesis cannot be closed.
# (()               False       Every opening parenthesis must be closed.
# (()())            True
# ())(()            False       An unclosed parenthesis cannot be closed.

def paranthesis(key):
    
    count= 0

    for i in key:
        if count == 0 and i == ")":
            return False
        if i == "(":
            count += 1
        elif i == ")":
            count -=1
    if count == 0:
        return True
    elif count!= 0:
        return False
        
paranthesis()
