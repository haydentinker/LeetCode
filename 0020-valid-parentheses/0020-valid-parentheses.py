class Solution:
    def isValid(self, s: str) -> bool:
        myStack=[]
        for i in s:
            if (i=='(') or (i=='{') or (i=='['):
                myStack.append(i)
            else:
                if not myStack:
                    return False
                else:
                    if i ==']':
                        if not myStack.pop()=='[':
                            return False
                    elif i ==')':
                        if not myStack.pop()=='(':
                            return False 
                    elif i=='}':
                        if not myStack.pop()=='{':
                            return False 
        if myStack:
            return False 
        return True            