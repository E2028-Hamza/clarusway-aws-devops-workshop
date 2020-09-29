def is_valid_parenthese(str1):
    stack = [] 
    pchar = {"(": ")", "{": "}", "[": "]"}
    for i in str1:
        if i in pchar:
            stack.append(i)
        elif len(stack) == 0 or pchar[stack.pop()] != i:
            return False
    return len(stack) == 0

print(is_valid_parenthese("()"))
print(is_valid_parenthese("()[]{}"))
print(is_valid_parenthese("(]"))
print(is_valid_parenthese("([)]"))
print(is_valid_parenthese("{[]}"))
print(is_valid_parenthese(""))