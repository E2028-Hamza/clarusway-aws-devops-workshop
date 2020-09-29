def isValid(s):
        openP = ["[", "{", "("]
        closeP = ["]", "}", ")"]
        stack = []
        
        for c in s.strip():
            if c in openP:
                stack.append(c)
            
            if c in closeP:
                if len(stack) == 0: 
                    return False
                if openP.index(stack.pop()) != closeP.index(c):
                    return False
                    
        if len(stack) > 0:
            return False
            
        return True

s = "([)]"
print(isValid(s))