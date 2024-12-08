def isValid(s: str) -> bool:
    parentheses = {')': '(', '}': '{', ']': '['}
    stack = []
    for i in s:
        if i in parentheses.values():
            stack.append(i)
        else:
            if not stack or stack.pop() != parentheses[i]:
                return False
        
    return not stack

print(isValid("()[]{}"))
print(isValid("({[})"))
print(isValid("(]"))
