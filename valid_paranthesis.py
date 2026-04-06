def valid_parenthesis(s):
    parenthesis = {"{": "}", "(": ")", "[": "]"}
    stack = []
    opening_parenthesis = set("({[")
    for each_char in s:
        if each_char in opening_parenthesis:
            stack.append(each_char)
        else:
            if not stack:
                return False
            comp = stack.pop()
            if parenthesis[comp] != each_char:
                return False
    return True if not stack else False


print(valid_parenthesis("(({}))"))   # True
print(valid_parenthesis("{(())}}"))  # False
