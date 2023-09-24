class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for item in s:
            if item == '(' or item == '{' or item == '[':
                stack.append(item)
            else:
                if not stack:
                    return False

                else:
            
                    if item == ')':
                        if stack.pop()!='(':
                            return False
                    
                    elif item == '}':
                        if stack.pop()!='{':
                            return False
                    else:
                        if item == ']':
                            if stack.pop()!='[':
                                return False     
        if stack:          
            return False
        return True


